from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([MenuItem, Table,  OrderItem])

@admin.register(Order)  #yo models.py ko order ho hai parameter ma vako 
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["table","created_at","status","total"]
    list_editable = ["status"]
    search_fields = ['table__name']
    list_filter = ["status"]