from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        return f" {self.name} ({self.email})"
    
class MyResume(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title



    