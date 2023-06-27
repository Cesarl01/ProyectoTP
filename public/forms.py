from django import forms
from .models import Persona
from .models import Persona

class ContactForm(forms.Form):
    # class Meta:
    #     model: Persona
        fields = ['nombre','apellido','email','dni']
        nombre = forms.CharField(
                    label='Nombre', 
                    max_length=50,
                    #validators=(solo_caracteres,),
                    widget=forms.TextInput(
                            attrs={'class':'form-control',
                                'placeholder':'Solo letras'}
                            )
                )
        apellido = forms.CharField(
                    label='Apellido', 
                    max_length=50,
                    #validators=(solo_caracteres,),
                    widget=forms.TextInput(
                            attrs={'class':'form-control',
                                'placeholder':'Solo letras aquí'}
                            )
                )     
        email = forms.EmailField(
                    label='Email',
                    max_length=100,
                    required=False,
                    #validators=(validate_email,),
                    error_messages={
                            'required': 'Por favor completa el campo'
                        },
                    widget=forms.TextInput(attrs={'class':'form-control','type':'email'})
                )     
        dni = forms.IntegerField(label='DNI')


        