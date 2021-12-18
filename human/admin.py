from django.contrib import admin
from .models import DetailsOfHuman, favouriteQuotes

# Register your models here.
@admin.register(DetailsOfHuman)
class DetailsOfHumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'favourite_food']

@admin.register(favouriteQuotes)
class FavouriteOfAdmin(admin.ModelAdmin):
    list_display = ['user_f_quotes', 'quote']
