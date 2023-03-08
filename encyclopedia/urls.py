from django.urls import path

from . import views

app_name="encl"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.MtoH, name="mtoh"),
    path("new", views.New, name="New"),
    path("wiki/<str:name>/edite", views.edite, name="edite"),
    path("random", views.random1, name="random"),
    path("wiki/<str:name>/delete", views.delete, name="delete"),
]
