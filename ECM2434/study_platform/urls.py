from django.urls import path
from . import views
from . import forms

app_name = 'study_platform'
urlpatterns = [
    path('', views.home_view, name='home'),           #Will be changed to home page when made
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('shop/', views.shop, name='shop'),
    path('create_card', views.create_card, name='create_card'),
    path('answer_quiz/',views.answer_quiz, name='answer_quiz')
]
