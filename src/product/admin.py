from django.contrib import admin
from .models import Category, Product, UserBucket, Bucket

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserBucket)
admin.site.register(Bucket)
