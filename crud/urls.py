from django.urls import path
from crud.views import AtividadeHomeView, AtividadeAddView, AtividadeAttView, AtividadeVerView, AtividadeDelView

urlpatterns = [
    path('atividade/', AtividadeHomeView.as_view(), name='home_atividade'),
    path('atividade/add/', AtividadeAddView.as_view(), name='atividade_add'),
    path('atividade/<int:pk>/att/', AtividadeAttView.as_view(), name='atividade_att'),
    path('atividade/<int:pk>/ver/', AtividadeVerView.as_view(), name='atividade_ver'),
    path('atividade/<int:pk>/del/', AtividadeDelView.as_view(), name='atividade_del'),
]
