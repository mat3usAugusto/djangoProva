from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def medico(request):
    return render(request, 'medico.html')


def paciente(request):
    return render(request, 'paciente.html')


def consulta(request):
    return render(request, 'consulta.html')
