from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.index , name="index" ),
    path('projects/' , views.projects , name="projects" ),
    path('contact/' , views.contact , name="contact" ),
    path('feedback/' , views.feedback , name="feedback" ),
    path('about/' , views.about , name="about" ),
    path('mysirg2881928/' , views.ulogin , name="ulogin" ),
    path('ulogout/' , views.ulogout , name="ulogout" ),
]
