from django.urls import path
from .import views

urlpatterns = [
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('signup/' , views.signup, name = 'signup'),
    path('user_detail/' , views.user_detail, name = 'user_detail'),
    path('', views.post_list, name = 'post_list'),

]
