from django.shortcuts import render

# Create your views here.
import logging

from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ListCreateForm
from .models import ShoppingList

logger = logging.getLogger(__name__)


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class LocationView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'location.html'


class ListDisplayView(LoginRequiredMixin, generic.ListView):
    model = ShoppingList
    template_name = 'list_display.html'
    paginate_by = 5

    def get_queryset(self):
        products = ShoppingList.objects.filter(user=self.request.user).order_by('-created_at')
        return products


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = ShoppingList
    template_name = 'list_create.html'
    form_class = ListCreateForm
    success_url = reverse_lazy('listapp:list_display')

    def form_valid(self, form):
        listapp = form.save(commit=False)
        listapp.user = self.request.user
        listapp.save()
        messages.success(self.request, '買う物をリストに追加しました')
        return super().form_valid(form)


class ListDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ShoppingList
    template_name = 'list_delete.html'
    success_url = reverse_lazy('listapp:list_display')

    """ def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました')
        return super().delete(request, *args, **kwargs)"""
