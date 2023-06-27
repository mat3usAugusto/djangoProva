"""
URL configuration for Clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_clinica import views as clinicaHome
from app_clinica import views as clinicaMedico
from app_clinica import views as clinicaPaciente
from app_clinica import views as clinicaConsulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', clinicaHome.home, name='home'),
    path('medico/', clinicaMedico.medico, name='medico'),
    path('paciente/', clinicaPaciente.paciente, name='paciente'),
    path('consulta/', clinicaConsulta.consulta, name='consulta')
]
