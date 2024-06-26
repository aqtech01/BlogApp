from django.urls import path
from core.views import *

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("blog/<id>/",blog_details,name="blog_details"),
]