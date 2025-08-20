from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control", "placeholder": "What to do?"}),
            "deadline": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "is_done": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tags": forms.CheckboxSelectMultiple(),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tag name"}),
        }