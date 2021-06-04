from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50, null=True)
    country_of_origin = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.first_name +" "+ self.last_name



class Book(models.Model):
    title = models.CharField(max_length=50, null = True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, null = True)
    price = models.CharField(max_length=50, null = True)
    number_of_pages = models.CharField(max_length=50, null = True)
    language = models.CharField(max_length=50, null = True)
