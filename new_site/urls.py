from django.urls import path
from . import views
urlpatterns = [
path('posts/', views.new_site_all, name = 'posts' ),
]