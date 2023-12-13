from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', "thumb"]

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']

    def __init__(self, *args, **kwargs):
        super(UpdateArticleForm, self).__init__(*args, **kwargs)