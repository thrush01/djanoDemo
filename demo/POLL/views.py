from django.shortcuts import render,redirect
from items.models import Categories,Item

from .forms import SingupForm

# Create your views here.
def index(request):
    items= Item.objects.filter(is_sold=False)
    categories=Categories.objects.all()
    return render(request,'demo/index.html',{
                  'categories':categories,
                  'items':items,})

def content(request):
    return render(request,'demo/content.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SingupForm()

    return render(request,'demo/signup.html',{  
        'form':form
    })

