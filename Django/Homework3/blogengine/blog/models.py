from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    surname = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=150,unique=True)

    def __str__(self):
        return '{}'.format(self.name)