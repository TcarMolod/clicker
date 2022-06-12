from django.urls import path
from . import views
from .views import *
from django.contrib import admin

boosts = BoostViewSet.as_view({ 
    'get': 'list',
    'post': 'create'
})

lonely_boost = BoostViewSet.as_view({
    'put': 'partial_update',
})

urlpatterns = [
    path('', index, name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('call_click/', call_click, name='call_click'),
    path('boosts/', boosts, name='boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost'),
    path('update_coins/', update_coins, name='update_coins'),
    path('core/', get_core, name='get_core'),
]