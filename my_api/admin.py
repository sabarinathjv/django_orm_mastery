from django.contrib import admin
from .models import *


admin.site.register(Post)

admin.site.register(Teacher)

admin.site.register(Student)

# admin.site.register(Product)#in the 3

admin.site.register(Book)#in the 3rd method we cant direcly use the product table

admin.site.register(Cupboard)
