from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# Create your views here.
class HomeView(TemplateView):
    template_name = "contextapp/index.html"
    context = {}

    # Get request 
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)