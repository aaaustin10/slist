from django.views.generic import TemplateView, ListView
from slist.models import *

class index(TemplateView):
    template_name = "index.html"

class lists(ListView):
    context_object_name = "lists"
    template_name = "lists.html"

    def get_queryset(self):
        return List.objects.filter(owner=self.request.user)

class list(lists):
    pass
