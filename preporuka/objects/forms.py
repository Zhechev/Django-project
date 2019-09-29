from django import forms
from .models import Object, Comment


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = [
            'category',
            'title',
            'address',
            'content',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
