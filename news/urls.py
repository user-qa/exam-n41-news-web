from django.urls import path

from news.views import PostNewsView, get_news_details_view, WriteCommentView, delete_comment_view, delete_news_view

app_name = 'news'

urlpatterns = [
    path('add/', PostNewsView.as_view(), name='add'),
    path('details/<int:pk>/', get_news_details_view, name='details'),
    path('comments/', WriteCommentView.as_view(), name='comment'),
    path('delete/comment/<int:pk>/', delete_comment_view, name='delete_comment'),
    path('delete/news/<int:pk>/', delete_news_view, name='delete_news')
]
