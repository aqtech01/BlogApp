from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="core/images", default="")  # removed "media/" from the upload_to path
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)  # changed to auto_now_add=True for creation timestamp
    deleted_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)  # set null and blank to True for optional field
    
    def __str__(self):
        return self.title
