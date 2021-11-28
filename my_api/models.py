from django.db import models
from django.contrib.auth.models import AbstractUser, User



class Post(models.Model):
    title = models.CharField(max_length=250)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')


    def __str__(self):
        return self.title  


###############orm explore


class Teacher(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student(models.Model):
      
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname  




###################################solution for db design cupboard and book 
#1.use induvidual tables (not efficient)
#################################################
# 2.multi table inheritance eg:

# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', default='images/default.png')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Book(Product):#when look in admin can see the fileds of products also and can add data
#     publisher = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)


# class Cupboard(Product):#when look in admin can see the fileds of products also and can add data
#     shelves = models.IntegerField()
#     author = models.CharField(max_length=255)


#########################################################################    
#solution 3 abstract models 

#################################################
# 2.multi table inheritance eg:

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(Product):#when look in admin can see the fileds of products also and can add data
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)


class Cupboard(Product):#when look in admin can see the fileds of products also and can add data
    shelves = models.IntegerField()
    author = models.CharField(max_length=255)


                
