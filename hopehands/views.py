from django.shortcuts import render


def home(request):
    return render(request,"hopehands/index.html")
# Create your views here.
def about(request):
    return render(request,"hopehands/aboutus.html")
def volunteer(request):
    return render(request,"hopehands/volunteer.html")