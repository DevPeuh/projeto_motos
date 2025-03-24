from django.shortcuts import render # Renderiza uma resposta http e devolve uma HttpResponse para o usuário
from bikes.models import Bike


def bikes_view(request):
    bikes = Bike.objects.all() # Busca todos os objetos dentro do banco de dados do modelos - A Mesma coisa que fazer no SQL: SELECT * FROM Bike

    return render(
        request, # Requisição do usuário
        'bikes.html', # Conecta com o html feito
        {'bikes': bikes}
    ) # Primeiro passando a requisição do usuário, depois o caminho


