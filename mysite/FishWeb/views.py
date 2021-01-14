from django.shortcuts import render

from django.views.generic import ListView, View

from .models import Item


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class ProductView(View):
    def get(self, request):
        return render(request, 'products.html')

class StoreView(View):
    def get(self, request):
        city = "Russia, Ekaterinburg, Mira 32"
        return render(request, 'store.html', {'city': city,})

class FishView(ListView):
    model = Item
    template_name = 'product.html'
