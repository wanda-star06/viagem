from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela_inicial, name='tela_inicial'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destinos/novo/', views.cria_destino, name='cria_destino'),
    path('destinos/<int:pk>/editar/', views.edita_destino, name='edita_destino'),
    path('destinos/<int:pk>/deletar/', views.deleta_destino, name='deleta_destino'),
    path('pacotes/', views.lista_pacotes, name='lista_pacotes'),
    path('pacotes/novo/', views.cria_pacote, name='cria_pacote'),
    path('pacotes/<int:pk>/editar/', views.edita_pacote, name='edita_pacote'),
    path('pacotes/<int:pk>/deletar/', views.deleta_pacote, name='deleta_pacote'),
]
