from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def inicio(request):
    form = RegForm()
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "el_form" : form,
    }
    return render(request, "inicio.html", context)