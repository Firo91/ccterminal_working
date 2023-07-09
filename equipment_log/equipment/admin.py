from django.contrib import admin
from .models import Equipment, CheckHistory,CustomUser, EquipmentEditHistory

# Register your models here.

admin.site.register(Equipment)
admin.site.register(CheckHistory)
admin.site.register(CustomUser)
admin.site.register(EquipmentEditHistory)