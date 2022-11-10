from django.shortcuts import render
from . import models
# Create your views here.
def new_site_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_main.html', {'post': post})