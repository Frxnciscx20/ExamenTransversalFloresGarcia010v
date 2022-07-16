from django.contrib import admin
from django.urls import path
from django.urls import include
from products.views import ProductListView 
from .views import index, feriados, formContacto, formReg, fotos, productos, qsomos, form_mod_cliente, form_mod_producto, form_crear_cliente, form_crear_producto, mostrar, mostrar2,  form_del_cliente, form_del_producto, botonera
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[ 
    path ('', index, name="index"),
    path ('feriados/', feriados, name="feriados"),
    path ('formContacto/', formContacto, name="formContacto"),
    path ('formReg/', formReg, name="formReg"),
    path ('fotos/', fotos, name="fotos"),
    path ('usuarios/registro', views.registro, name='registro'),
    path ('usuarios/login',views.login,name='login'),
    path ('productos/', ProductListView.as_view(), name="productos"),
    path ('qsomos/', qsomos, name="qsomos"),
    path ('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path ('form_crear_producto/', form_crear_producto, name="form_crear_producto"), 
    path ('mostrar/', mostrar, name="mostrar"),
    path ('mostrar2/', mostrar2, name="mostrar2"),
    path ('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path ('botonera/', botonera, name="botonera"),
    path ('productos2/', include('products.urls')),
    path ('carrito/', include('carts.urls'))



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)