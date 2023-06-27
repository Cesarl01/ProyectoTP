from django.shortcuts import render, redirect
from django.http import HttpResponse
from public.forms import ContactForm
from public.models import Persona

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola, realizando salida de hola_mundo del ProyectoTP')

def index(request):
    if (request.method == 'GET'):
        titulo = 'Está accediendo por método GET'
       
    else:
        titulo = 'Esta accediendo por otro método diferente a GET'        
    
    parametro_1 = request.GET.get('param_1')
    parametro_2 = request.GET.get('param_2')
    return render(request,'public/index.html',{'titulo':titulo})
    # return HttpResponse(f"""<h1>Entrando en el proyecto de Django ProyectoTP</h1>    
    #         <p>1er Parámetro: {parametro_1}</p>
    #         <p>2do Parámetro: {parametro_2}</p>
    # """)

def bebidas(request):    
    return render(request,'public/bebidas.html')

def carrusel(request):
    return render(request,'public/carrusel.html')

def contacto(request):
    mensaje=None
    #listado_cursos = None
    if (request.method == 'POST'):
        contacto_form = ContactForm(request.POST)
        if(contacto_form.is_valid()):  
            contacto_form.save()
            mensaje = 'Información recibida y enviada'
            return redirect('public/contacto.html')
        else:    
            mensaje = 'Problemas con el envío'
    else:        
        contacto_form = ContactForm()         
        
    # context = {                
    #             'mensaje': mensaje,            
    #             'contacto_form':contacto_form
    #         }
    return render(request,'public/index_test.html',{'contacto_form':contacto_form})

def jamones(request):
    return render(request,'public/jamones.html')

def opiniones(request):
    return render(request,'public/opiniones.html')

def quesos(request):
    return render(request,'public/quesos.html')

def saludar(request,nombre):
    return HttpResponse(f"""
    <h1>Hola {nombre}</h1>
        
    <p>Esta es una prueba de url con parámetro</p>

    """
    )

def ver_proyectos(request,anio,mes):
    return HttpResponse(f"""
    <h1>Estos son los proyectos del mes {mes} y año {anio}</h1>

    <p>Esta es una prueba de url para la función de proyectos</p>

    """
    )
