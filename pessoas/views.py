from django.shortcuts import render
from pessoas.models import Pessoa
from django.utils import timezone
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

class CreatePessoa(CreateView):
    model = Pessoa
    fields = ['nome','sobrenome','idade']
    success_url = '/pessoas/pessoas/'

class UpdatePessoa(UpdateView):
    model = Pessoa
    fields = ['nome','sobrenome','idade']
    success_url = '/pessoas/pessoas/'

class PessoaView(ListView):
    model = Pessoa
    paginate_by = 2

class DetalhesPessoas(DetailView):
    model = Pessoa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = timezone.now()
        return context

class DeletePessoa(DeleteView):
    model = Pessoa
    success_url = '/pessoas/pessoas/'

