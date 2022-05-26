from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entries_url, name="entries"),
    # path("random", views.random_entry, name="random"),
    path("add", views.add_entry, name="add")
]
