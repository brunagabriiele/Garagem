
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from core.views import CategoriaViewSet, CarroViewSet, MarcaViewSet

router.register(r'categorias', CategoriaViewSet)
router.register(r'Carro', CarroViewSet)
router.register(r'Marca', MarcaViewSet)

...