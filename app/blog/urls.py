from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/like_detail', views.like_detail, name='like-detail'),
    path('user_detail/<int:pk>', views.user_detail, name='user-detail')
]