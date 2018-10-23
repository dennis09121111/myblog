from django import forms
from django.contrib.auth.models import User
from .models import Review
from post.models import Post

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)


# class ReviewUpdateForm(forms.Form):
#     class meta:
#         model = Review
#         fields = ('content',)
