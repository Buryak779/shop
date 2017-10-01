from django.contrib import admin
from .models import *


# class SubscriberAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Subscriber._meta.fields]
#     list_filter = ['name',]# Фильтр по имени
#     fields = ['email']
#     search_fields = ['name', 'email'] #Создаем поле ввода поиска по имени и емайлу
#
# admin.site.register(Subscriber, SubscriberAdmin)

