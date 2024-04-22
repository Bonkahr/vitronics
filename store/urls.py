from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:id>", views.filter_by_category, name="filtered"),
]
