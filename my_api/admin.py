# from django.contrib import admin
# from .models import *


# admin.site.register(Post)

# admin.site.register(Teacher)

# admin.site.register(Student)

# # admin.site.register(Product)#in2 we can register , in the 3 we cant register

# admin.site.register(Product)

# admin.site.register(Book)#in the 3rd method we cant direcly use the product table

# admin.site.register(Cupboard)

# admin.site.register(Category)


#below soln 4 
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import Product, Book, Cupboard ,Mybook

class ModelAChildAdmin(PolymorphicChildModelAdmin):

    base_model = Product

@admin.register(Book)
class ProductAdmin(ModelAChildAdmin):
    base_model = Book  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site

@admin.register(Cupboard)
class ProductAdmin(ModelAChildAdmin):
    base_model = Cupboard  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Product)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product  # Optional, explicitly set here.
    child_models = (Book, Cupboard)



admin.site.register(Mybook)


