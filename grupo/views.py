from io import BytesIO
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Grupo
from django.db import transaction
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.urls import reverse_lazy
from datetime import date


class GruposView(ListView):
    
    model = Grupo
    template_name = 'grupo/grupos.html'
    
    
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
        

class CrearGrupoView(CreateView):
    
    model = Grupo
    template_name = 'grupo/creacion_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
    
    @transaction.atomic
    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class EliminarGrupoView(DeleteView):
    
    model = Grupo
    template_name = 'grupo/eliminar_grupo.html'
    success_url = reverse_lazy('lista_grupos')


class EditarGrupoView(UpdateView):
    
    model = Grupo
    template_name = 'grupo/editar_grupo.html'
    fields = ('nombre_grupo', 'descripcion',)
