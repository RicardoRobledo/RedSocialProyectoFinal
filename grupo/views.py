from io import BytesIO
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Grupo, MiVista
from django.db import transaction
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.urls import reverse_lazy
from datetime import date
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class GruposView(LoginRequiredMixin, ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'


def obtener_grafico():
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    
    return graph


@login_required
def grafica(request):
    
    usuarios = []
    cantidad_grupos = []
    
    # Aplicando uso de vista
    for i in list(MiVista.objects.all().values()):
        
        usuarios.append(i['username'])
        cantidad_grupos.append(i['cantidad_grupos'])
    
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,6))
    plt.title('Cantidad de grupos por usuario')
    plt.plot(usuarios, cantidad_grupos)
    plt.xticks(rotation=45)
    plt.xlabel('usuarios')
    plt.ylabel('cantidad de grupos')
    plt.tight_layout()
    
    return render(request, 'grupo/grafica.html', {'chart': obtener_grafico()})


@login_required
def reporte(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    
    c.setLineWidth(.3)
    c.setFont('Helvetica-Bold', 22)
    c.drawString(30,750, 'QuAi')
    c.setFont('Helvetica', 12)
    c.drawString(30,735, 'Reporte')
    c.setFont('Helvetica', 12)
    c.drawString(480, 750, str(date.today()))
    
    c.line(460, 747, 560, 747)
    
    datos = Grupo.objects.all()
    fila=600
    
    for dato in datos:
        c.drawString(30, fila, str(dato.id))
        c.drawString(100, fila, str(dato))
        c.drawString(200, fila, str(dato.propietario))
        c.drawString(300, fila, str(dato.fecha))
        fila-=40
    
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    
    return response
        

class CrearGrupoView(LoginRequiredMixin, CreateView):
    
    model = Grupo
    template_name = 'grupo/creacion_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
    
    @transaction.atomic
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class EliminarGrupoView(LoginRequiredMixin, DeleteView):
    
    model = Grupo
    template_name = 'grupo/eliminar_grupo.html'
    success_url = reverse_lazy('lista_grupos')


class EditarGrupoView(LoginRequiredMixin, UpdateView):
    
    model = Grupo
    template_name = 'grupo/editar_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
