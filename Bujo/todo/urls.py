from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home' ),
    # path('name/',views.name, name='name'),
    path('profile/', views.profile, name='profile'),
    path('this_week/', views.week, name='week'),
    path('key/', views.key, name='key')

]