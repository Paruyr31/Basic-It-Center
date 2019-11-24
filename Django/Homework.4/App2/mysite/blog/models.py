from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    price = models.CharField(max_length=150,db_index=True)
    details = models.TextField()
    owner = models.CharField(max_length=150)
    registered_date = models.DateTimeField(default=timezone.now)