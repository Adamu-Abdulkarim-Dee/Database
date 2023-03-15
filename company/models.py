from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'password']

    def __str__(self):
        return "{}".format(self.email)



class SchoolBoard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100)
    p_o_box = models.CharField(max_length=50)
    school_batch = models.ImageField(upload_to='batch', default='school_batch.jpg')
    school_address = models.CharField(max_length=50)
    school_owner_name = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=50, blank=True, null=True)
    location = CountryField()

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.school_name)   

class Contact(models.Model):
    descriptions = models.TextField(max_length=200)
    image = models.ImageField(upload_to='complaints')
    school_name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.school_name)