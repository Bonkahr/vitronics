from nis import cat
from django.shortcuts import render

from .models import Category, Product

# Create your views here.


def home(request):

    categories = Category.objects.all()
    products = Product.objects.all().order_by("-created_on")

    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "home.html", context)
