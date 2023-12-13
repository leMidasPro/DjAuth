from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.art_lst, name='list'),
    path('create/', views.art_create, name='create'),
    path('edit/<int:article_id>/', views.art_edit, name='edit'),
    path('<slug:slug>/', views.art_det, name='detail'),
]
