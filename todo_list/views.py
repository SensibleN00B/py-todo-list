from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task, Tag
from .forms import TaskForm, TagForm


class IndexView(ListView):
    model = Task
    template_name = "todo_list/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return (
            Task.objects.all()
            .prefetch_related("tags")
            .order_by("is_done", "-created_at")
        )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("index")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo_list/confirm_delete.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["cancel_url"] = reverse_lazy("index")
        return ctx


class TaskToggleView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("index")


class TagListView(ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"
    context_object_name = "tags"
    ordering = ("name",)


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo_list/confirm_delete.html"
    success_url = reverse_lazy("tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse_lazy("tag-list")
        return context