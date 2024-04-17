from django.contrib import admin
from .models import Product

class Lista_itens(admin.ModelAdmin):
    list_display = ('id','description','price','data_compra')


admin.site.register(Product,Lista_itens)
