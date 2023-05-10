from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def inicio(request):
    form = RegForm()
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data.get("email"))
        print(form_data.get("nombre"))
    context = {
        "el_form" : form,
    }
    return render(request, "inicio.html", context)