from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("hope", views.hope, name="Elina"),
    path("trust", views.trust, name="Vera"),
    path("love", views.love, name="Elvira"),
    path("<str:name>", views.greet, name="greet")
]