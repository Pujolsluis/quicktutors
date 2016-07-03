from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'subject', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })
