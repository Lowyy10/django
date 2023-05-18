from django.conf import settings
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.

def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "titulo" : titulo,
        "el_form" : form,
    }
    

    if form.is_valid():
        instance = form.save(commit=False)
        nombre=form.cleaned_data.get("nombre")
        email=form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "PERSONA"
        #form_data = form.cleaned_data
        instance.save()
        context = {
            "titulo": "Gracias %s!" %(nombre)
        }
        if not nombre:
            context={
                "titulo": "Gracias persona sin nombre"
            }
        print(instance)
        print(instance.timestamp)
        #abc = (form_data.get("email"))
        #abc2 = (form_data.get("nombre"))
        #obj = Registrado.objects.create(email=abc, nombre=abc2)

    return render(request, "inicio.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.items():
        #    print(key, value)
        form_email = form.cleaned_data.get=("email")
        form_mensaje = form.cleaned_data.get=("mensaje")
        form_nombre = form.cleaned_data.get=("nombre")
        asunto = 'Form de Contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from,  "otroemail@gmail.com"]
        email_mensaje = "%s: $s enviado por $S" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            mensaje_email,
            email_from,
            email_to,
            fail_silently=True)
    context = {
        "form": form,
    }
    return render(request, "forms.html", context)