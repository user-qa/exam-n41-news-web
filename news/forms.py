from django import forms
from news.models import NewsModel

class PostNewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['headline', 'content', 'photo', 'category']


