from django.urls import path, include
from . import views

urlpatterns = [
    path('doctorslog',views.logfun,name='login'),
    path('dochome',views.homefun,name='dhome')
]
