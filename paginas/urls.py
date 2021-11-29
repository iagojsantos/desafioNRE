from django.urls import path
from .views import indexView

urlpatterns = [
    path('inicio/', indexView.as_view(), name= 'inicio'),
    #todas as vezes que crio o path eu tenho que sguir esse caminho (endereço que desejo, minha view.as_viewe, e depois o nome que quero chamar essa view)
]