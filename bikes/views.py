from django.shortcuts import render, redirect # Renderiza uma resposta http e devolve uma HttpResponse para o usuário
from bikes.models import Bike
from .forms import BikeModelForm
from django.views import View


class BikeView(View):

    def get(self, request): 
        bikes = Bike.objects.all().order_by('model') 
        search = request.GET.get('search') 

        if search:
            bikes = Bike.objects.filter(model__icontains = search) # Filtra a busca que usuário passou, "icontains" é para ignorar maiúsculas ou minúsculas

        return render(request, 'bikes.html', {'bikes': bikes}) # Pega a requisição do usuário, vai conectar com o html feito e passar os dados python para o html


def new_bike_view(request):
    if request.method == 'POST':
        new_bike_form = BikeModelForm(request.POST, request.FILES) # Cria um novo formulário com os dados que o usuário passou, request.POST é para pegar os dados do formulário e request.FILES é para pegar os arquivos que o usuário passou, como a imagem
        if new_bike_form.is_valid():
            new_bike_form.save()
            return redirect('bikes_list') # Redireciona para a lista de motos cadastradas
    elif request.method == 'GET':
        new_bike_form = BikeModelForm() # Retorna o formulário vazio
    return render(request, 'new_bike.html', { 'new_bike_form': new_bike_form }) # Renderiza o template new_bike.html e passa o formulário para ele  
