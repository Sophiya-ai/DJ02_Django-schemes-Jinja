from django.urls import path
from . import views
# . импорт из той папки, в которой находимся


urlpatterns = [
    path('data/',views.data),
    path('test/', views.test),
]