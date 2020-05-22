from django.shortcuts import render, redirect

# Create your views here.


def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'index.html')
