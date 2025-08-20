from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.order_by("name"),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
