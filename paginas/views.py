from django.views.generic import TemplateView


# Create your views here.
class InicioPageView(TemplateView):
    
    template_name = 'paginas/inicio.html'
