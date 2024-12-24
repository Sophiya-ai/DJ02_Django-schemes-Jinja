from django.urls import path
from . import views
# . импорт из той папки, в которой находимся


urlpatterns = [
    path('workWithStatic/',views.wStatic, name='wStatic'),
    path('pros/', views.pros_cons, name='pros'),
    path('test/', views.test),
    path('test/', views.test),
]