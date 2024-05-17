from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from news.forms import PostNewsForm
from news.models import CategoryModel, NewsModel, CommentsModel


# ------------------------------------------------Post Details View-----------------------------------------------------

class PostNewsView(LoginRequiredMixin, CreateView):
    template_name = 'news/add-news.html'
    form_class = PostNewsForm

    def get_context_data(self, **kwargs):
        categories = CategoryModel.objects.all()
        context = {
            'categories': categories
        }

        return context

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def form_valid(self, form):
        current_news = form.save(commit=False)
        current_news.posted_by = self.request.user
        current_news.save()
        messages.success(self.request, 'News posted successfully!')
        return redirect('pages:home')

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect('news:add')


# ------------------------------------------------News Details View-----------------------------------------------------

def get_news_details_view(request, pk):
    news = NewsModel.objects.filter(id=pk).first()
    comments = CommentsModel.objects.filter(tagged_news=pk).order_by('created_at')
    context = {
        'news': news,
        'comments': comments,
    }
    if news:
        return render(request, 'news/news-details.html', context=context)
    else:
        return render(request, 'news/news-not-found.html')


# ------------------------------------------------Comment to the News---------------------------------------------------

class WriteCommentView(LoginRequiredMixin, View):
    def post(self, request):
        message = request.POST.get('comment')
        written_by = request.user
        tagged_news_id = request.POST.get('news_id')
        tagged_news = NewsModel.objects.get(id=tagged_news_id)

        CommentsModel.objects.create(
            message=message,
            written_by=written_by,
            tagged_news=tagged_news
        )

        return redirect('news:details', pk=tagged_news_id)


# ---------------------------------------------------Delete Comment-----------------------------------------------------

def delete_comment_view(request, pk):
    comment = CommentsModel.objects.filter(id=pk).first()
    print(comment)
    tagged_news = NewsModel.objects.get(id=comment.tagged_news.id)
    comment.delete()

    return redirect('news:details', pk=tagged_news.id)


# ---------------------------------------------------Delete News--------------------------------------------------------
def delete_news_view(request, pk):
    news = NewsModel.objects.filter(id=pk).first()
    news.delete()

    return redirect('pages:home')