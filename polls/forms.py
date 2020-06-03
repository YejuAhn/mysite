from django import forms
from .models import Question, Choice, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']







