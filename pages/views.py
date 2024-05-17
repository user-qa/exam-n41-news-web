from django.shortcuts import render

from news.models import NewsModel


def home_page_view(request):
    template_name = 'news/home.html'
    news = NewsModel.objects.all().order_by('-created_at')
    q = request.GET.get('q')
    if q:
        news = NewsModel.objects.filter(headline__icontains=q).order_by('-created_at')
    context = {
        'breaking_news': news[:3],
        'newss': news
    }

    return render(request, template_name=template_name, context=context)
