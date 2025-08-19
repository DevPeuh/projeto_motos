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


class NewBikeView(View):
    def get(self, request):
        new_bike_form = BikeModelForm()
        return render(request, 'new_bike_html', {'new_bike_form': new_bike_form}) # Renderiza o template new_bike.html e passa o formulário para ele
    
    def post(self, request):
        new_bike_form = BikeModelForm(request.POST, request.FILES)
        if new_bike_form.is_valid():
            new_bike_form.save()
            return redirect('bike_list')
        return render(request, 'new_bike_html', {'new_bike_form': new_bike_form})
    
class BikeDetailView(View):
    pass