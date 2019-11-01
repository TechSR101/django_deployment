from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('register/', views.register, name='register'),
    path('user_login',views.user_login, name='user_login'),
]
