from rest_framework import serializers
from .models import Entrega


class EntregSerie(serializers.ModelSerializer):

    class Meta:
        model = Entrega
        fields = ['produto', 'status', 'data','foto']
       