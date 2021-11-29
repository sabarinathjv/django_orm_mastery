from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from polymorphic.models import PolymorphicModel


class Mybook(models.Model):
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cost = models.BigIntegerField()

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
#solution 3 abstract models  #not workin to me

#################################################


# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)

#     class Meta:
#         verbose_name_plural = 'categories'

#     def get_absolute_url(self):
#         return reverse('store:category_list', args=[self.slug])

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,
#     limit_choices_to={'models_in':('book','cupboard,')})
#     object_id  = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type','object_id')
#     class Meta:
#         ordering = ['object_id']



# class Base(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', default='images/default.png')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class Book(Base):#when look in admin can see the fileds of products also and can add data
#     publisher = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     m2m = models.ManyToManyField(Product,related_name="store_book_related",related_query_name="book",)

# class Cupboard(Base):#when look in admin can see the fileds of products also and can add data
#     shelves = models.IntegerField()
#     author = models.CharField(max_length=255)
#     m2m = models.ManyToManyField(Product,related_name="store_cupboard_related",related_query_name="cupboard",)


#####################soln 3 ends


#####################soln 4 polymorphic model


# class Category(models.Model):
#     name = models.CharField(max_length=255, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True)

#     class Meta:
#         verbose_name_plural = 'categories'

#     def get_absolute_url(self):
#         return reverse('store:category_list', args=[self.slug])

#     def __str__(self):
#         return self.name



# class Product(PolymorphicModel):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to='images/', default='images/default.png')
#     slug = models.SlugField(max_length=255)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#     in_stock = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


# class Book(Product):
#     publisher = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)


# class Cupboard(Product):
#     shelves = models.IntegerField()
#     author = models.CharField(max_length=255)







                
