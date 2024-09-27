from django.urls import path
from .views import PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView

urlpatterns = [
    path('', PaisListView.as_view(), name='pais_list'),  # Esta ruta maneja /paises/
    path('nuevo/', PaisCreateView.as_view(), name='pais_create'),
    path('editar/<int:pk>/', PaisUpdateView.as_view(), name='pais_update'),
    path('eliminar/<int:pk>/', PaisDeleteView.as_view(), name='pais_delete'),
]