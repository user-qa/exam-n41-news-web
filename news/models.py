from django.db import models

from users.models import UserModel


class CategoryModel(models.Model):
    category = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    def __repr__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class NewsModel(models.Model):
    headline = models.TextField()
    content = models.TextField()
    photo = models.ImageField(upload_to='news-photos')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)

    posted_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

    def __repr__(self):
        return self.headline

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



class CommentsModel(models.Model):
    message = models.TextField()
    written_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    tagged_news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
