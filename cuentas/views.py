from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class RegistroPageView(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('iniciosesion')
    template_name = 'cuentas/registro.html'
