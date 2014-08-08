from django.views.generic import TemplateView, ListView

class index(TemplateView):
  template_name = "index.html"

class lists(ListView):
  context_object_name = "lists"
  template_name = "lists.html"
  def get_queryset(self):
    return []
