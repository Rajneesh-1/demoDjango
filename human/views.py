import requests
from django.shortcuts import render, redirect, HttpResponseRedirect
from human.models import DetailsOfHuman
from human.forms import formDetails
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        favourite_food = request.POST['favourite_food']

        """To Create New Instance/objects of DetailsOfHuman"""
        instanceOfDetails = DetailsOfHuman.objects.create(name=name, city=city, favourite_food=favourite_food)
        """To Save New Instance/objects of DetailsOfHuman"""
        instanceOfDetails.save()

    '''To Show All objects of DetailsOfHuman'''
    getSavedDetails = DetailsOfHuman.objects.all()
    print("getSavedDetails", getSavedDetails)

    """
        '''To Show Only selected object of DetailsOfHuman using get'''
        getSavedDetails = DetailsOfHuman.objects.get(id=33)
        print("getSavedDetails", getSavedDetails)
    """

    """
        '''To Show Only selected object of DetailsOfHuman using filter'''
        getSavedDetails = DetailsOfHuman.objects.get(id=33)
        print("getSavedDetails", getSavedDetails)
    """

    return render(request, 'homeHTML/home.html', {"getSavedDetails": getSavedDetails})


def login(request):
    return render(request, 'loginHTML/login.html')

def edit_data(request, id):
    if request.method == "POST":

        """Provide a id to edit/Update objects of that Id"""
        getDataToEdit = DetailsOfHuman.objects.get(id=id)
        data = formDetails(request.POST, instance=getDataToEdit)
        data.save()
        messages.success(request, "Your Data Edited Successfully !")

        """check for sub path in root url"""
        return HttpResponseRedirect('/')

    else:
        getDataToEdit = DetailsOfHuman.objects.get(id=id)
        data = formDetails(instance=getDataToEdit)

    getSavedDetails = DetailsOfHuman.objects.all()
    return render(request, 'homeHTML/home.html', {"corm": data, "getSavedDetails": getSavedDetails})


def delete_data(request, id):
    print(id)
    if request.method == "POST":
        deleteSavedDetails = DetailsOfHuman.objects.get(id=id)
        deleteSavedDetails.delete()

    getSavedDetails = DetailsOfHuman.objects.all()
    """check for name in root url"""
    #return redirect("homeHTML")

    return render(request, "homeHTML/home.html", {"getSavedDetails": getSavedDetails})
