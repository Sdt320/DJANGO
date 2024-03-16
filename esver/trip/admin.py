from django.contrib import admin
from .models import *

class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name','image','descripition')

admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product)

# Register your models here.
