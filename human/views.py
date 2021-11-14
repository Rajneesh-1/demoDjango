import requests
from django.shortcuts import render,HttpResponseRedirect
from human.models import DetailsOfHuman

# Create your views here.
def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        favourite_food = request.POST['favourite_food']

        recieved_data = []
        recieved_data.append(name)
        recieved_data.append(city)
        recieved_data.append(favourite_food)

        instanceOfDetails = DetailsOfHuman.objects.create(name=name, city=city, favourite_food=favourite_food)
        instanceOfDetails.save()

    getSavedDetails = DetailsOfHuman.objects.all()
    print("getSavedDetails", getSavedDetails)

    return render(request, 'homeHTML/home.html',{"getSavedDetails": getSavedDetails})

def login(request):

    return render(request, 'loginHTML/login.html')
