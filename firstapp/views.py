from django.shortcuts import render
from backend.models import maincategory

# Create your views here.

def home(request):

    mydata = maincategory.objects.all().values()

    return render(request, 'index.html',{'data':mydata})

def fashion(request):

    mydata = maincategory.objects.all().values()

    return render(request, 'fashion.html',{'data':mydata})

def jewellery(request):

    mydata = maincategory.objects.all().values()

    return render(request, 'jewellery.html',{'data':mydata})

def electronic(request):

    mydata = maincategory.objects.all().values()

    return render(request, 'electronic.html',{'data':mydata})

def detail(request):

    mydata = maincategory.objects.all().values()

    return render(request, 'detail.html',{'data':mydata})