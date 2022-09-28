from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doces/', views.doces, name='doces'),
    path('salgadas/', views.salgadas, name='salgadas'),
    path('festas/', views.festas, name='festas'),
    path('cafe_lanches/', views.cafe_lanches, name='cafe_lanches'),
    path('post/<int:post_id>/', views.exibir_post, name='exibir_post'),
    path('autor/<int:autor_id>/', views.exibir_autor, name='exibir_autor'),
]