from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name_task', 'description', 'executor', 'date_completion', 'status']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

