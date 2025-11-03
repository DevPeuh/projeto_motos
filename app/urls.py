from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bikes.views import BikesListView, NewBikeCreateView, BikeDetailView, BikeUpdateView, BikeDeleteView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('bikes/', BikesListView.as_view(), name='bikes_list'), # as_view() converte a classe em view
    path('new_bike/', NewBikeCreateView.as_view(), name='new_bike'),
    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'), # pk é a chave primária que identifica o objeto
    path('bike/<int:pk>/update', BikeUpdateView.as_view(), name='bike_update'),
    path('bike/<int:pk>/delete', BikeDeleteView.as_view(), name='bike_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona a rota para acessar as imagens, o '+' é para concatenar a lista de rotas com a rota de imagens, o 'settings.MEDIA_URL' é a rota que vai ser acessada para ver as imagens e o 'settings.MEDIA_ROOT' é o diretório onde as imagens estão salvas.
