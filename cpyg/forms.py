from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente , Categoria
from django.contrib.auth.models import User



class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombre', 'marca', 'precio','imagen']
        labels ={
            'idProducto': 'idProducto', 
            'nombre': 'nombre', 
            'marca': 'marca', 
            'precio': 'precio',
            'imagen': 'imagen',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese idProducto', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            

        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'correo', 'telefono', 'direccion']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'direccion': 'Dirección', 
            
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Teléfono',
                    'id':'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Dirección',
                    'id': 'direccion'
                }
            ),
        
        }

class CategoriaForm(forms.ModelForm):

    class Meta: 
        model= Categoria
        fields = ['idCategoria', 'nombreCategoria']
        labels ={
            'idCategoria': 'ID', 
            'nombreCategoria': 'Nombre',

        }
        widgets={
            'idCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'ID', 
                    'id': 'idCategoria'
                }
            ), 
            'nombreCategoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre', 
                    'id': 'nombreCategoria'
                }
            )

        }


class Registro(forms.Form):
    
    username = forms.CharField(required=True, min_length=5, max_length=40)
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Ejemplo@gmail.com'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña'
    }))
    
    password2= forms.CharField(label='Confirmar contraseña' ,required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirmar contraseña'
    }))



    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exist():
            raise forms.ValidationError('Usuario ya creado')
        
        return username


    def clean_email(self):
        correo = self.cleaned_data.get('email')

        if User.objects.filter(email=correo).exist():
            raise forms.ValidationError('Correo ya registrado')
        
        return correo


    def clean(self):
        cleaned_data = super.clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'la contraseña no coincide')



    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )