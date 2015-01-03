from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from slist.models import *

class index(TemplateView):
    template_name = "index.html"

class lists(ListView):
    context_object_name = "lists"
    template_name = "lists.html"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)

    def post(self, request):
        List.objects.create(owner=self.request.user, name=self.request.POST['list_name'])
        return HttpResponseRedirect(self.request.path)

class list_page(lists):
    context_object_name = "items"
    template_name = "list.html"

    def get_queryset(self):
        return get_object_or_404(List, owner=self.request.user, pk=self.kwargs['list_id']).item_set.all()

    def get_context_data(self):
        context = super(list_page, self).get_context_data()
        context['lists'] = List.objects.filter(owner=self.request.user)
        return context

    def post(self, request, list_id):
        parent = get_object_or_404(List, owner=self.request.user, pk=self.kwargs['list_id'])
        Item.objects.create(parent=parent, name=self.request.POST['item_name'], quantity=1, unit_cost=1, units=1)
        return HttpResponseRedirect(self.request.path)
