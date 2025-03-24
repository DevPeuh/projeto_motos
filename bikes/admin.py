from django.contrib import admin
from bikes.models import Bike, Brand

class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) # Exibe o nome da marca
    search_fields = ('name',) # Pesquisa pelo nome da marca


admin.site.register(Brand, BrandAdmin)
admin.site.register(Bike, BikeAdmin)