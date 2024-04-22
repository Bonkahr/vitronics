from django.shortcuts import render

from .models import Category, Product


def home(request):

    categories = Category.objects.all()
    products = Product.objects.all().order_by("-created_on")

    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "home.html", context)


def filter_by_category(request, id: str):
    category = Category.objects.filter(id=id).first()
    categories = Category.objects.all()
    products = Product.objects.all().filter(category=category).order_by("-created_on")

    context = {"products": products, "categories": categories, "category": category}

    return render(request, "filtered-category.html", context)
