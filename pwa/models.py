from django.db import models
from django.db.models import Q
from datetime import date

ENTREGA = [('Em espera', 'Em Espera'), ('Entregue', 'Entregue')]

class Product(models.Model):
    name = models.CharField('Nome do Produto',max_length=255)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço',max_digits=10, decimal_places=2)
    data_compra = models.DateField('Data da Compra')
    

    def __str__(self):
        return "nome:%s, descrip:%s " % (self.name, self.description)

def limit_date_choices():
        return Q(data_compra=date.today()) | Q(name__startswith='Sa')

class Entrega(models.Model):
    produto = models.OneToOneField(Product, 
                                   related_name='remessa',
                                   on_delete=models.CASCADE, 
                                   verbose_name='lista de entrega',
                                   limit_choices_to=limit_date_choices,
                                   )
    status = models.CharField(max_length=100, choices=ENTREGA)
    foto = models.ImageField(upload_to='foto/')
    data = models.DateField('criado em')

    def __str__(self):
        return "comprovante:%s, status:%s " % (self.produto, self.status)
