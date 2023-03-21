from rest_framework.serializers import ModelSerializer

from livraria.models import  LivroSerializer, Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroDetalheSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1