from django.urls import path
from . import views


app_name='posts' #네임 스페이스


urlpatterns= [
    path("", views.i_list, name='list'),
    path("posts/create", views.i_create , name='create'),
    path("posts/<int:pk>/update", views.i_update , name='update'),
    path("posts/<int:pk>/delete", views.i_delete,name='delete'),
    path("posts/<int:pk>", views.i_detail,name='detail'),
    path("posts/tool", views.t_list, name='t_list'),
    path("posts/tool/create", views.t_create , name='t_create'),
    path("posts/tool/<int:pk>", views.t_detail,name='t_detail'),
    path("posts/tool/<int:pk>/delete", views.t_delete,name='t_delete'),
    path("posts/tool/<int:pk>/update", views.t_update , name='t_update'),
   
]