from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.text import slugify
from jsignature.fields import JSignatureField
from phonenumber_field.modelfields import PhoneNumberField


class PrimaryAlbum(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,
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
    user = models.ForeignKey(User,
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

class SchoolBoard(models.Model):
    user = models.ForeignKey(User,
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

class Paymentistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    is_subscribe = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class ResultClass(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)   

class SectionPrimary(models.Model):
    attendance = models.CharField(max_length=18, blank=True, null=True)
    name = models.CharField(max_length=50)

    english_language_ca = models.IntegerField()
    english_language_exam = models.IntegerField()
    english_total = models.IntegerField()
    english_language_grade = models.CharField(max_length=3, blank=True, null=True)
    english_language_remark = models.CharField(max_length=18, blank=True, null=True)

    mathematics_ca = models.IntegerField()
    mathematics_exam = models.IntegerField()
    mathematics_total = models.IntegerField()
    mathematics_grade = models.CharField(max_length=3)
    mathematics_remark = models.CharField(max_length=18)

    computer_ca = models.IntegerField()
    computer_exams = models.IntegerField()
    computer_total = models.IntegerField()
    computer_grade = models.CharField(max_length=3)
    computer_remark = models.CharField(max_length=18)

    science_ca = models.IntegerField()
    science_exam = models.IntegerField()
    science_total = models.IntegerField()
    science_grade = models.CharField(max_length=3)
    science_remark = models.CharField(max_length=18)

    social_studies_ca = models.IntegerField(blank=True, null=True)
    social_studies_exam = models.IntegerField(blank=True, null=True)
    social_studies_total = models.IntegerField(blank=True, null=True)
    social_studies_grade = models.CharField(max_length=3,blank=True, null=True)
    social_studies_remark = models.CharField(max_length=18,blank=True, null=True)

    language_ca = models.IntegerField(blank=True, null=True)
    language_exam = models.IntegerField(blank=True, null=True)
    language_total = models.IntegerField(blank=True, null=True)
    language_grade = models.CharField(max_length=3,blank=True, null=True)
    language_remark = models.CharField(max_length=18,blank=True, null=True)

    physical_education_ca = models.IntegerField(blank=True, null=True)
    physical_education_exam = models.IntegerField(blank=True, null=True)
    physical_education_total = models.IntegerField(blank=True, null=True)
    physical_education_grade = models.CharField(max_length=3,blank=True, null=True)
    physical_education_remark = models.CharField(max_length=18,blank=True, null=True)

    history_ca = models.IntegerField(blank=True, null=True)
    history_exam = models.IntegerField(blank=True, null=True)
    history_total = models.IntegerField(blank=True, null=True)
    history_grade = models.CharField(max_length=3,blank=True, null=True)
    history_remark = models.CharField(max_length=18,blank=True, null=True)

    fiqh_ca = models.IntegerField(blank=True, null=True)
    fiqh_exam = models.IntegerField(blank=True, null=True)
    fiqh_total  = models.IntegerField(blank=True, null=True)
    fiqh_grade = models.CharField(max_length=3,blank=True, null=True)
    fiqh_remark = models.CharField(max_length=18,blank=True, null=True)

    tawheed_ca = models.IntegerField(blank=True, null=True)
    tawheed_exam = models.IntegerField(blank=True, null=True)
    tawheed_total = models.IntegerField(blank=True, null=True)
    tawheed_grade = models.CharField(max_length=3,blank=True, null=True)
    tawheed_remark = models.CharField(max_length=18,blank=True, null=True)

    arabic_language_ca = models.IntegerField(blank=True, null=True)
    arabic_language_exam = models.IntegerField(blank=True, null=True)
    arabic_language_total = models.IntegerField(blank=True, null=True)
    arabic_language_grade = models.CharField(max_length=3,blank=True, null=True)
    arabic_language_remark = models.CharField(max_length=18,blank=True, null=True)

    quran_ca = models.IntegerField(blank=True, null=True)
    quran_exam = models.IntegerField(blank=True, null=True)
    quran_total = models.IntegerField(blank=True, null=True)
    quran_grade = models.CharField(blank=True, null=True, max_length=3)
    quran_remark = models.CharField(blank=True, null=True, max_length=18)


    tahfidz_ca =  models.IntegerField(blank=True, null=True)
    tahfidz_exam = models.IntegerField(blank=True, null=True)
    tahfidz_total = models.IntegerField(blank=True, null=True)
    tahfidz_grade = models.CharField(blank=True, null=True, max_length=3)
    tahfidz_remark = models.CharField(blank=True, null=True, max_length=18)

    agriculture_ca = models.IntegerField(blank=True, null=True)
    agriculture_exam = models.IntegerField(blank=True, null=True)
    agriculture_total = models.IntegerField(blank=True, null=True)
    agriculture_grade = models.CharField(blank=True, null=True, max_length=3)
    agriculture_remark = models.CharField(blank=True, null=True, max_length=18)

    civic_education_ca = models.IntegerField(blank=True, null=True)
    civic_education_exam = models.IntegerField(blank=True, null=True)
    civic_education_total = models.IntegerField(blank=True, null=True)
    civic_education_grade = models.CharField(blank=True, null=True, max_length=3)
    civic_education_remark = models.CharField(blank=True, null=True, max_length=18)

    class_of = models.ForeignKey(ResultClass, on_delete=models.CASCADE)
    terms = models.CharField(blank=True, null=True, max_length=10 )
    year = models.CharField(blank=True, null=True, max_length=10)

    position = models.CharField(blank=True, null=True, max_length=10)

    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.class_of) 