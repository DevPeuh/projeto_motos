from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bikes.views import bikes_view, new_bike_view
from accounts.views import register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('bikes/', bikes_view, name='bikes_list'), 
    path('new_bike/', new_bike_view, name='new_bike'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona a rota para acessar as imagens, o '+' é para concatenar a lista de rotas com a rota de imagens, o 'settings.MEDIA_URL' é a rota que vai ser acessada para ver as imagens e o 'settings.MEDIA_ROOT' é o diretório onde as imagens estão salvas.
