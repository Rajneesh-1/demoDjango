import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from human.models import DetailsOfHuman, favouriteQuotes
from human.forms import formDetails
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        if (request.POST['name'] != " "):
            name = request.POST['name']
            city = request.POST['city']
            favourite_food = request.POST['favourite_food']

            checkNameInsideDB = DetailsOfHuman.objects.filter(name=request.POST['name'])
            if (len(checkNameInsideDB) != 0):
                isNameOfThisUserPresent = True
            else:
                isNameOfThisUserPresent = False
                instanceOfDetails = DetailsOfHuman.objects.create(name=name, city=city, favourite_food=favourite_food)
                instanceOfDetails.save()
        else:
            name = request.POST['name'] + " " + request.POST['middleName']
            city = request.POST['city']
            favourite_food = request.POST['favourite_food']
            instanceOfDetails = DetailsOfHuman.objects.create(name=name, city=city, favourite_food=favourite_food)
            instanceOfDetails.save()
            isNameOfThisUserPresent = False

        """To Create New Instance/objects of DetailsOfHuman"""
        # instanceOfDetails = DetailsOfHuman.objects.create(name=name, city=city, favourite_food=favourite_food)
        """To Save New Instance/objects of DetailsOfHuman"""
        # instanceOfDetails.save()


    else:
        isNameOfThisUserPresent = False

    '''To Show All objects of DetailsOfHuman'''
    getSavedDetails = DetailsOfHuman.objects.all()
    getFovouriteQoutesDetails = favouriteQuotes.objects.all()
    tempDict={}
    for i in getFovouriteQoutesDetails:
        y = DetailsOfHuman.objects.get(id=i.user_f_quotes_id)
        tempDict[y.name] = i.quote
        print("favourite quotes by user ----> ",tempDict) # name ---> rohit, qoute ---> "how"

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
    return render(request, 'homeHTML/home.html',
                  {"getSavedDetails": getSavedDetails, "isNameOfThisUserPresent": isNameOfThisUserPresent,"favoriteQoutesAndName": tempDict})


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
    # return redirect("homeHTML")

    return render(request, "homeHTML/home.html", {"getSavedDetails": getSavedDetails})

def showFavouriteQoutesTextBox(request):
    print("-----------------------------------------------------------------------------------------")
    if request.method == 'POST':
        print("request.POST --------------------> ", request.POST)
        peopleName = request.POST['peopleName']
        quotes = request.POST['quotes']
        no_of_quotes = request.POST['quotesCount']
        print("||no_of_quotes||", no_of_quotes)
        getUser = DetailsOfHuman.objects.filter(name = peopleName)
        print(getUser)
        for i in getUser:
            print(i.id)
            saveFavouriteQuotes = favouriteQuotes(quote=request.POST['quotes'], user_f_quotes_id = i.id)
            saveFavouriteQuotes.save()
        return JsonResponse({})
