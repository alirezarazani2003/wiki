from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>/",views.detail, name="detail"),
    path("wiki/<str:name>/edit",views.edit, name="edit"),
]
