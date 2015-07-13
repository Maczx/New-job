from django.shortcuts import render
from blog.models import *






# Create your views here.
def home(request):
  if request.method == 'POST':
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    blog = Blog()
    blog.title = title
    blog.content = content
    blog.save()
    bloglist = Blog.objects.all()
    return render(request,'home.html',{'bloglist':bloglist})
  elif request.method == 'GET':
    bloglist = Blog.objects.all()
    return render(request,'home.html',{'bloglist':bloglist})
