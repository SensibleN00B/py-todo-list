from django.urls import path, include

from todo_list import views

app_name = "todo_list"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.TaskToggleView.as_view(), name="task-toggle"),

    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]
