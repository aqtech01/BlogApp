from django.shortcuts import render,get_object_or_404
from core.models import *

# Create your views here.
def home(request):
    data = Blog.objects.all()
    context = {
        "data":data,
        "title":"Home",
    }

    return render(request, "core/index.html",context)
def blog_details(request, id):
    data = get_object_or_404(Blog, pk=id)
    context = {
        "data": data,
        "title": "Blog Details",
    }
    return render(request, "core/blog_details.html", context)
    
def contact(request):
    return render(request, "core/contact.html")
def about(request):
    return render(request, "core/about.html")
