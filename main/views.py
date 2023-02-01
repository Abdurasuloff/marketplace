from django.shortcuts import render
from django.views import View
from products.models import Product, Category
from django.shortcuts import get_object_or_404
# Create your views here.

def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories":categories}

class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        q=request.GET.get('q', '')
        if q:
            products = products.filter(title__icontains=q)
        return render(request, "index.html", {'products':products})
    
class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        q=request.GET.get('q', '')
        if q:
            products = products.filter(title__icontains=q)
        return render(request, "category.html", {'products':products, "category":category})  