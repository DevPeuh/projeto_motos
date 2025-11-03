from bikes.models import Bike
from .forms import BikeModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class BikesListView(ListView):
    model = Bike
    template_name = 'bikes.html'
    context_object_name = 'bikes' 

    def get_queryset(self):
        # Super() puxa da ListView
        bike = super().get_queryset().order_by('model') # get_queryset retorna um queryset de objetos Bike ordenados pelo campo 'model'
        search = self.request.GET.get('search')
        if search:
            bike = bike.filter(model__icontains=search) #icontains é para ignorar maiúsculas ou minúsculas
        return bike
    
class NewBikeCreateView(CreateView):
    model = Bike
    form_class = BikeModelForm
    template_name = 'new_bike.html'
    success_url = '/bikes/'

 
class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'

class BikeUpdateView(UpdateView):
    model = Bike
    form_class = BikeModelForm
    template_name = 'bike_update.html'

    def get_success_url(self):
        return reverse_lazy('bike_detail', kwargs={'pk': self.object.pk})

class BikeDeleteView(DeleteView):
    model = Bike
    template_name = 'bike_delete.html'
    success_url = '/bikes/'
