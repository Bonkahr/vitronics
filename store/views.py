from django.shortcuts import get_object_or_404, render

from .models import Category, Product, ProductImages


def home(request):

    categories = Category.objects.all()
    products = Product.objects.all().order_by("-created_on")

    context = {
        "categories": categories,
        "products": products,
    }

    return render(request, "home.html", context)


def filter_by_category(request, id: int):
    category = Category.objects.filter(id=id).first()
    categories = Category.objects.all()
    products = Product.objects.all().filter(category=category).order_by("-created_on")

    context = {"products": products, "categories": categories, "category": category}

    return render(request, "filtered-category.html", context)


def product_detail(request, id: int):
    categories = Category.objects.all()
    product = []
    try:
        product = get_object_or_404(Product, id=id)
        photos = ProductImages.objects.filter(product=product)
        context = {
            'product': product,
            'photos': photos,
            'categories': categories,
        }

        return render(request, 'product-detail.html', context)
    except:
        context = {
            'product': product,
            'categories': categories,
        }
        return render(request, 'product-detail.html', context)
