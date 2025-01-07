from django.db import models

# Create your models here.
class Education(models.Model):
    clzname = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)


class Experience(models.Model):
    companyname = models.CharField(max_length=50)
    position = models.CharField(max_length=50, default=None)
    address = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

class Skills(models.Model):
    language = models.CharField(max_length=50)
    percent = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    degree = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    positionDetail = models.TextField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.TextField()
    type = models.CharField(max_length=50)   #web app / mobile app
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, blank=True, null=True)
    subject = models.CharField(max_length=100 , blank=True, null=True)  
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)






