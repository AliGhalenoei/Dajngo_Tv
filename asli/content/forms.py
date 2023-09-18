from django import forms
from .models import *

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('comment',)

class UpdateCommentSeryalForm(forms.ModelForm):
    class Meta:
        model = CommentSeryal
        fields=('comment',)


