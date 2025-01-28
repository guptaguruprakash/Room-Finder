from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('nav/',views.nav,name='nav'),
    path('body/',views.body,name='body'),
    
    
 path("__reload__/", include("django_browser_reload.urls")),#removed after production
]