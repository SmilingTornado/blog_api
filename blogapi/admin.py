from django.contrib import admin
from .models import Card

# Register your models here.

admin.site.register(Card)

class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ['name','category',]
    search_fields = ['name','category']