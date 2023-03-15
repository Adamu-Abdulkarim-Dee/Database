from email.mime import image
from django.db import models
from company.models import User
from django_countries.fields import CountryField
from django.utils.text import slugify
from jsignature.fields import JSignatureField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class PrimaryAlbum(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return str(self.name)        

class Primary(models.Model):
    admission_number = models.CharField(max_length=40)
    profile_picture = models.FileField(upload_to='image')
    first_name =models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    address_of_student = models.CharField(max_length=50)
    class_Of_student = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=10)
    RELIGION_CHOICE = (
        ('Islam', 'Islam'),
        ('Christianity', 'Christianity'),
        ('Atheism', 'Atheism'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Judaism', 'Judaism'),
        ('Catholicism', 'Catholicism'),
        ('Rastafari', 'Rastafari'),
        ('Agnostic', 'Agnostic'),
        ('Other', 'Other'),
    )
    religion = models.CharField(max_length=25, choices=RELIGION_CHOICE)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    year_of_graduation = models.ForeignKey(PrimaryAlbum, on_delete=models.CASCADE)
    signature_of_student = JSignatureField()
    comment_of_student = models.TextField(blank=True, null=True, max_length=50)
    nationality_of_student = CountryField()
    state_of_student = models.CharField(max_length=30)
    local_government_of_student = models.CharField(max_length=50)
    certificate_of_birth_photo = models.ImageField(upload_to='image')
    residential_certificate_photo = models.ImageField(upload_to='image')


    #Guadians
    name_of_guardian = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True)
    address_of_guardian = models.CharField(max_length=50)
    nationality_of_guardian = CountryField()
    state_of_guardian = models.CharField(max_length=50)
    local_government_of_guardian = models.CharField(max_length=50)
    occupation_of_guardian = models.CharField(max_length=50)
    work_address = models.CharField(max_length=50)
    relationship = models.CharField(max_length=25)
    signature_of_guardian = JSignatureField()
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.last_name)

class SecondaryAlbum(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)        

class Secondary(models.Model):
    admission_number = models.CharField(max_length=1000)
    profile_picture = models.FileField(upload_to='image')
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES)  
    address_of_student = models.CharField(max_length=100)
    class_Of_student = models.CharField(max_length=40)
    date_of_birth = models.DateField(max_length=10)
    RELIGION_CHOICE = (
        ('Islam', 'Islam'),
        ('Christianity', 'Christianity'),
        ('Atheism', 'Atheism'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Judaism', 'Judaism'),
        ('Catholicism', 'Catholicism'),
        ('Rastafari', 'Rastafari'),
        ('Agnostic', 'Agnostic'),
        ('Other', 'Other'),
    )
    religion = models.CharField(max_length=25, choices=RELIGION_CHOICE)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    year_of_graduation = models.ForeignKey(SecondaryAlbum, on_delete=models.CASCADE)
    signature_of_student = JSignatureField()
    comment_of_student = models.TextField(blank=True, null=True, max_length=50)
    nationality_of_student = CountryField()
    state_of_student = models.CharField(max_length=30)
    local_government_of_student = models.CharField(max_length=50)
    certificate_of_birth_photo = models.ImageField(upload_to='image')
    residential_certificate_photo = models.ImageField(upload_to='image')

    #Guadians
    name_of_guardian = models.CharField(max_length=30)
    phone_number = PhoneNumberField(blank=True)
    address_of_guardian = models.CharField(max_length=50)
    nationality_of_guardian = CountryField()
    state_of_guardian = models.CharField(max_length=30)
    local_government_of_guardian = models.CharField(max_length=50)
    occupation_of_guardian = models.CharField(max_length=50)
    work_address = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    signature_of_guardian = JSignatureField()
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return str(self.last_name)    

