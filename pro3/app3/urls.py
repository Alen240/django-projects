
from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup1,name='signup'),
    path('login/',views.login1,name='login') ,
    path('logout/',views.logout1,name='logout'),  
]
