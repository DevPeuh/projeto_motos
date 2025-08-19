from django.shortcuts import render, redirect # Renderiza uma resposta http e devolve uma HttpResponse para o usuário
from bikes.models import Bike
from .forms import BikeModelForm
from django.views import View
from django.views.generic import ListView


class BikesListView(ListView):
    model = Bike
    template_name = 'bikes.html'
    context_object_name = 'bikes' 

    def get_queryset(self):
        # Super() puxa da ListView
        bike = super().get_queryset().order_by('model') # Ordena as motos pelo modelo
        search = self.request.GET.get('search')
        if search:
            bike = bike.filter(model__icontains=search) #icontains é para ignorar maiúsculas ou minúsculas
        return bike

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