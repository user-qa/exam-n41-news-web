from django.contrib import admin
from news.models import NewsModel, CategoryModel, CommentsModel

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['headline', 'posted_by', 'created_at']
    search_fields = ['headline', 'posted_by', 'created_at', 'content']
    list_filter = ['headline', 'posted_by', 'created_at', 'content']


@admin.register(CategoryModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'created_at']
    search_fields = ['category', 'created_at']
    list_filter = ['category', 'created_at']


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['message', 'created_at']
    search_fields = ['message', 'created_at']
    list_filter = ['message', 'created_at']
