from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'homeHTML/home.html')


def login(request):
    x = ["RAJNEESH", "Monu"]
    return render(request, 'loginHTML/login.html', {"Data": x})
