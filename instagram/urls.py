from django.urls import path,include
from . import  views

app_name = 'instagram'

urlpatterns = [
    path('post/new/', views.post_new, name = 'post_new'),
]
