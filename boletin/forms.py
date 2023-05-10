from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model=Registrado
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio,extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Correo no Valido")
        return email

        
class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()