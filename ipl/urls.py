from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('login/',views.admin_login , name = 'admin_login'),
    path('logout/',views.admin_logout,name = 'admin_logout')
    
]
