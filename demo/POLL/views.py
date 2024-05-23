from django.shortcuts import render
from items.models import Categories,Item
# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Categories.objects.all()

    return render(request,'demo/index.html',{
        'items':items,
        'categories':categories,
    })

def content(request):
    return render(request,'demo/index.html')