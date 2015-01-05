from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from slist.models import *

class index(TemplateView):
    template_name = "index.html"

class lists(ListView):
    context_object_name = "lists"
    template_name = "lists.html"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)

    def post(self, request):
        list_name = self.request.POST['list_name']
        if len(list_name.split()) != 0:
            List.objects.create(owner=self.request.user, name=list_name)
        return HttpResponseRedirect(self.request.path)

class items(TemplateView):
    template_name = "items.html"

    def get_context_data(self, list_id):
        context = super(items, self).get_context_data()
        context['list'] = get_object_or_404(List, owner=self.request.user, pk=self.kwargs['list_id'])
        context['items'] = context['list'].item_set.all()
        context['lists'] = List.objects.filter(owner=self.request.user)
        return context

    def post(self, request, list_id):
        action = self.request.POST.get('action')
        redirect_path = self.request.path
        parent = get_object_or_404(List, owner=self.request.user, pk=self.kwargs['list_id'])
        if action == 'create':
            item_name = self.request.POST['item_name']
            if len(item_name.split()) != 0:
                Item.objects.create(parent=parent, name=item_name, quantity=1, unit_cost=1, units=1)
        elif action == 'delete_items':
            Item.objects.filter(parent=parent, id__in=self.request.POST.getlist('item_names[]')).delete()
        elif action == 'delete_list':
            parent.delete()
            redirect_path = reverse('lists')
        return HttpResponse(redirect_path)
