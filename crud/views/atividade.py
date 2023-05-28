from crud.models import Atividade
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy


class AtividadeHomeView(ListView):
    model = Atividade
    queryset = Atividade.objects.all()
    template_name = 'crud/home_atividade.html'


class AtividadeAddView(CreateView):
    model = Atividade
    fields = ['titulo', 'descricao']
    template_name = 'crud/atividade_add.html'
    # No reverse_lazy utilizar o nome dado na url
    success_url = reverse_lazy('atividade_add')


class AtividadeAttView(UpdateView):
    model = Atividade
    fields = ['titulo', 'descricao']
    template_name = 'crud/atividade_add.html'
    success_url = reverse_lazy('atividade_att')


class AtividadeVerView(DetailView):
    model = Atividade
    tamplate_name = 'crud/atividade_detail.html'
    # Como é definido este context automaticamente? quando uso 'atividade' sem ele, ainda funciona
    context_object_name = 'atividade'


class AtividadeDelView(DeleteView):
    queryset = Atividade.objects.all()
    success_url = reverse_lazy('home_atividade')
