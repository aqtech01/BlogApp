from django.shortcuts import render,get_object_or_404,redirect
from core.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    data = Blog.objects.all()
    context = {
        "data":data,
        "title":"Home",
    }

    return render(request, "core/index.html",context)
def blog_details(request, id):
    data = Blog.objects.get(id=id)
    print(data,id,data.desc)
    context = {
        "data": data,
        "title": "Blog Details",
    }
    return render(request, "core/blog_details.html", context)
    
def contact(request):
    if request.method == "POST":
        data = request.POST
        try:
            email = data.get("email")
            message = data.get("message")
            if not message and not email:
                messages.error(request, "Both field are Required")
            else:
                details = Contact.objects.create(email=email,message=message)
                details.save()
                messages.success(request, "Message Sent Successfully")
                return redirect("contact")
        except Contact.DoesNotExist as e:
            return f"Error:{e}"
    return render(request, "core/contact.html",{"title": "Contact"})
def about(request):
    return render(request, "core/about.html")
