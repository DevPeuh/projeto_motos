from django.shortcuts import render, redirect # Renderiza uma resposta http e devolve uma HttpResponse para o usuário
from bikes.models import Bike
from .forms import BikeModelForm


def bikes_view(request): # Os dados da requisição do usuário
    bikes = Bike.objects.all().order_by('model') # Busca todos os objetos, "order_by" é para ordenar a busca pelo modelo da moto

    # Caso tenha uma busca específica
    search = request.GET.get('search') # pega a requisição do usuário, captura o parâmetro search

    if search:   
        bikes = Bike.objects.filter(model__icontains=search) # Filtra a busca que usuário passou, "icontains" é para ignorar maiúsculas ou minúsculas
    return render(
        request, # Requisição do usuário
        'bikes.html', # Conecta com o html feito
        {'bikes': bikes}
    ) # Primeiro passando a requisição do usuário, depois o caminho


def new_bike_view(request):
    if request.method == 'POST':
        new_bike_form = BikeModelForm(request.POST, request.FILES) # Cria um novo formulário com os dados que o usuário passou, request.POST é para pegar os dados do formulário e request.FILES é para pegar os arquivos que o usuário passou, como a imagem
        if new_bike_form.is_valid():
            new_bike_form.save()
            return redirect('bikes_list') # Redireciona para a lista de motos cadastradas
    elif request.method == 'GET':
        new_bike_form = BikeModelForm() # Retorna o formulário vazio
    return render(request, 'new_bike.html', { 'new_bike_form': new_bike_form }) # Renderiza o template new_bike.html e passa o formulário para ele  
