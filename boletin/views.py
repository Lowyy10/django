from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def inicio(request):
    form = RegForm()
    if form.is_valid():
        form_data = form.cleaned_data
        abc = (form_data.get("email"))
        abc2 = (form_data.get("nombre"))
        obj = Registrado.objects.create(email=abc, nombre=abc2)
    context = {
        "el_form" : form,
    }
    return render(request, "inicio.html", context)