from django.urls import path
from . import views

urlptterns = [
    path('',views.blog_title),
]