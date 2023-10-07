from django.urls import path
from . import views

# this tells Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

