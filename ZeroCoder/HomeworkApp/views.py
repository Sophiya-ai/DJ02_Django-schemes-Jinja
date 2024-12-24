from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wStatic(request):
    context = {
        'question': 'Настройка статических файлов в Django',
        'active_page': 'wStatic'
    }
    return render(request, 'HomeworkApp/workWithStatic.html', context)

def pros_cons(request):
    context = {
        'question': 'Перимущества и недостатки Django',
        'active_page': 'benefits'
    }
    return render(request, 'HomeworkApp/index.html', context)
