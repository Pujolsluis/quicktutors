from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'subject', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
