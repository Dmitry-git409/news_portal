from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['to_author', 'select_field', 'to_category', 'title', 'content', 'post_rating']

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError ('No more 200 chars')
