from django.shortcuts import render
from django.http import HttpResponse

# Controlador que recebe requisição

def index (request):
    return HttpResponse('<h1>Olá Mundo</h1>')

