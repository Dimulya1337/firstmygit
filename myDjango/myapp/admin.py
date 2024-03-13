from django.contrib import admin
from myapp.models import beer

class beerProps(admin.ModelAdmin):
    list_display = ["taste","turnover"]
    
admin.site.register(beer,beerProps)

    



















# Register your models here.
