import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from conf.settings import EMAIL_HOST_USER
from users.forms import UserModelForm, LoginForm, UserUpdateForm
from users.models import ConfirmationCodeModel, UserModel


def send_email(email):
    code = random.randint(1000, 9999)
    active_codes = ConfirmationCodeModel.objects.filter(is_active=True)
    if active_codes.filter(code=code):
        send_email(email)
    subject = 'Confirmation email'
    receivers = [email]
    from_email = EMAIL_HOST_USER
    if send_mail(message=str(code), subject=subject, recipient_list=receivers, from_email=from_email):
        ConfirmationCodeModel.objects.create(
            code=code,
            email=email,
            is_active=True,
        )
        return True
    else:
        return False


class RegisterView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserModelForm

    def form_valid(self, form):
        current_user = form.save(commit=False)
        data = form.cleaned_data
        current_user.is_active = False
        current_user.set_password(data.get("password1"))
        current_user.save()
        if send_email(data.get("email")):
            return render(self.request, 'users/confirmation.html')
        else:
            messages.error(request=self.request,
                           message='Email could not be sent, try later again!')
            return redirect("users:register")

    def form_invalid(self, form):
        messages.error(request=self.request,
                       message=form.errors)
        return redirect("users:register")


class ConfirmEmailCodeView(View):
    def get(self, request):
        return render(request, 'users/confirmation.html')

    def post(self, request):
        inserted_code = request.POST.get('code')
        active_codes = ConfirmationCodeModel.objects.filter(is_active=True)
        sent_code = active_codes.filter(code=inserted_code).first()
        if sent_code:
            sent_code.is_active = False
            sent_code.save()
            current_user = UserModel.objects.filter(email=sent_code.email).first()
            current_user.is_active = True
            current_user.save()
            return redirect('users:login')

        else:
            messages.error(request, 'Wrong code. Please check your inbox again.')
            return redirect('users:confirm')


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login-page.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request=request, user=user)
                return redirect("pages:home")

        messages.error(request, 'Wrong password or email.')
        return redirect("users:login")


def logout_view(request):
    logout(request)
    return redirect('pages:home')


def user_detail_view(request, pk):
    target_user = UserModel.objects.get(id=pk)
    if target_user:
        return render(request, 'users/user-detail.html', context={'user': target_user})
    else:
        return render(request, 'users/user-not-found-page.html', context={'user': target_user})


class UpdateDetail(LoginRequiredMixin, View):
    def post(self, request, pk):
        current_user = UserModel.objects.filter(id=pk).first()
        form = UserUpdateForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('users:details', pk=pk)
        else:
            messages.error(request, form.errors)
            return redirect('users:update', pk=pk)

    def get(self, request, pk):
        current_user = UserModel.objects.filter(id=pk).first()
        return render(request, 'users/update-profile.html', context={'current_user': current_user})
