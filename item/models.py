from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to='category',blank=True,null=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural ='Categories'
    def __str__(self):
        return self.name   
class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,blank=True,null=True,default="no address yet")
    description = models.CharField(max_length=1000,blank=True,null=True)
    price = models.FloatField(max_length=255)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  

    

    def __str__(self):
        return self.name  