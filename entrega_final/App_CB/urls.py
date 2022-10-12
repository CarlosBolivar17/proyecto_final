from django.urls import path
from entrega_final.views import *
from App_CB.views import *
from entrega_final.settings import *


urlpatterns = [

    path('', inicio, name="inicio"),
]