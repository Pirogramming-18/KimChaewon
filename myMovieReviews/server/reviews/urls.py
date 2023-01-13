from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:movie_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    
]