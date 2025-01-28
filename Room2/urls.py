from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('')
    
 path("__reload__/", include("django_browser_reload.urls")),#removed after production
]