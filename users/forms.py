from django import forms
from users.models import UserModel


class UserModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=64)
    password2 = forms.CharField(max_length=64)

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'photo', 'phone_number','date_of_birth','password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'photo', 'phone_number','date_of_birth']