from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data(request):
    return HttpResponse('<h1> Здесь будет основная информация по моему проекту на Django </h1>')

def test(request):
    return HttpResponse('<h1> Тестирование моего проекта на Django </h1>')
