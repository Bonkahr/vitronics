from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:id>", views.filter_by_category, name="filtered"),
    path("product/<int:id>", views.product_detail, name='product-detail'),
]
