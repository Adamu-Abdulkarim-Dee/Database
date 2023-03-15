from django.db import models
from django.utils.text import slugify
from django.conf import settings
from company.models import User

# Create your models here.
class PrimaryResult(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name) 

class Primary(models.Model):
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

    class_of = models.ForeignKey(PrimaryResult, on_delete=models.CASCADE)
    terms = models.CharField(blank=True, null=True, max_length=10 )
    TERMS = (
        ('First', 'First'),
        ('Second', 'second'),
        ('Third', 'Third')
    )
    terms = models.CharField(max_length=100, choices=TERMS)

    position = models.CharField(blank=True, null=True, max_length=10)
    year = models.CharField(blank=True, null=True, max_length=50)

    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.class_of) 




















class AlbumS(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ScienceAlbums(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    albums = models.ForeignKey(AlbumS,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)


    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)
    def __str__(self):
        return str(self.name)   

class Science(models.Model):
    name = models.CharField(max_length=50)
    class_of = models.ForeignKey(ScienceAlbums, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, max_length=100)

    TERMS = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third')
    )
    terms = models.CharField(max_length=100, choices=TERMS)
    REMARK = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fail', 'Fail'),
        ('Pass', 'Pass')
    )
    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    english_language_ca = models.IntegerField(blank=True, null=True)
    english_language_exam = models.IntegerField(blank=True, null=True)
    english_language_total = models.IntegerField(blank=True, null=True)
    english_language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    english_language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    mathematics_ca = models.IntegerField(blank=True, null=True)
    mathematics_exam = models.IntegerField(blank=True, null=True)
    mathematics_total = models.IntegerField(blank=True, null=True)
    mathematics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    mathematics_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    physics_ca = models.IntegerField(blank=True, null=True)
    physics_exam = models.IntegerField(blank=True, null=True)
    physics_total = models.IntegerField(blank=True, null=True)
    physics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    physics_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    biology_ca = models.IntegerField(blank=True, null=True)
    biology_exam = models.IntegerField(blank=True, null=True)
    biology_total = models.IntegerField(blank=True, null=True)
    biology_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    biology_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    chemistry_ca = models.IntegerField(blank=True, null=True)
    chemistry_exam = models.IntegerField(blank=True, null=True)
    chemistry_total = models.IntegerField(blank=True, null=True)
    chemistry_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    chemistry_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    agricultural_science_ca = models.IntegerField(blank=True, null=True)
    agricultural_science_exam = models.IntegerField(blank=True, null=True)
    agricultural_science_total = models.IntegerField(blank=True, null=True)
    agricultural_science_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    agricultural_science_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    computer_ca = models.IntegerField(blank=True, null=True)
    computer_exam = models.IntegerField(blank=True, null=True)
    computer_total = models.IntegerField(blank=True, null=True)
    computer_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    computer_remark = models.CharField(max_length=100,null=True, blank=True, choices=REMARK)

    data_processing_ca = models.IntegerField(blank=True, null=True)
    data_processing_exam = models.IntegerField(blank=True, null=True)
    data_processing_total = models.IntegerField(blank=True, null=True)
    data_processing_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    data_processing_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    fisheries_ca = models.IntegerField(blank=True, null=True)
    fisheries_exam = models.IntegerField(blank=True, null=True)
    fisheries_total = models.IntegerField(blank=True, null=True)
    fisheries_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    fisheries_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    religion_ca = models.IntegerField(blank=True, null=True)
    religion_exam = models.IntegerField(blank=True, null=True)
    religion_total = models.IntegerField(blank=True, null=True)
    religion_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    religion_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    language_ca = models.IntegerField(blank=True, null=True)
    language_exam = models.IntegerField(blank=True, null=True)
    language_total = models.IntegerField(blank=True, null=True)
    language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    civic_education_ca = models.IntegerField(blank=True, null=True)
    civic_education_exam = models.IntegerField(blank=True, null=True)
    civic_education_total = models.IntegerField(blank=True, null=True)
    civic_education_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    civic_education_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    health_education_ca = models.IntegerField(blank=True, null=True)
    health_education_exam = models.IntegerField(blank=True, null=True)
    health_education_total = models.IntegerField(blank=True, null=True)
    health_education_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    health_education_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK) 

    tarikh_ca = models.IntegerField(blank=True, null=True)
    tarikh_exam = models.IntegerField(blank=True, null=True)
    tarikh_total = models.IntegerField(blank=True, null=True)
    tarikh_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    tarikh_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



























class AlbumA(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ArtAlbums(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    albums = models.ForeignKey(AlbumA,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Art(models.Model):
    name = models.CharField(max_length=50)
    class_of = models.ForeignKey(ArtAlbums, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, max_length=100)

    TERMS = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third')
    )
    terms = models.CharField(max_length=100, choices=TERMS)
    REMARK = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fail', 'Fail'),
        ('Pass', 'Pass')
    )
    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    english_language_ca = models.IntegerField(blank=True, null=True)
    english_language_exam = models.IntegerField(blank=True, null=True)
    english_language_total = models.IntegerField(blank=True, null=True)
    english_language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    english_language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    mathematics_ca = models.IntegerField(blank=True, null=True)
    mathematics_exam = models.IntegerField(blank=True, null=True)
    mathematics_total = models.IntegerField(blank=True, null=True)
    mathematics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    mathematics_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    government_ca = models.IntegerField(blank=True, null=True)
    government_exam = models.IntegerField(blank=True, null=True)
    government_total = models.IntegerField(blank=True, null=True)
    government_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    government_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    history_ca = models.IntegerField(blank=True, null=True)
    history_exam = models.IntegerField(blank=True, null=True)
    history_total = models.IntegerField(blank=True, null=True)
    history_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    history_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    economics_ca = models.IntegerField(blank=True, null=True)
    economics_exam = models.IntegerField(blank=True, null=True)
    economics_total = models.IntegerField(blank=True, null=True)
    economics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    economics_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    literature_ca = models.IntegerField(blank=True, null=True)
    literature_exam = models.IntegerField(blank=True, null=True)
    literature_total = models.IntegerField(blank=True, null=True)
    literature_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    literature_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    computer_ca = models.IntegerField(blank=True, null=True)
    computer_exam = models.IntegerField(blank=True, null=True)
    computer_total = models.IntegerField(blank=True, null=True)
    computer_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    computer_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    data_processing_ca = models.IntegerField(blank=True, null=True)
    data_processing_exam = models.IntegerField(blank=True, null=True)
    data_processing_total = models.IntegerField(blank=True, null=True)
    data_processing_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    data_processing_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    religion_ca = models.IntegerField(blank=True, null=True)
    religion_exam = models.IntegerField(blank=True, null=True)
    religion_total = models.IntegerField(blank=True, null=True)
    religion_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    religion_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    language_ca = models.IntegerField(blank=True, null=True)
    language_exam = models.IntegerField(blank=True, null=True)
    language_total = models.IntegerField(blank=True, null=True)
    language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    civic_education_ca = models.IntegerField(blank=True, null=True)
    civic_education_exam = models.IntegerField(blank=True, null=True,)
    civic_education_total = models.IntegerField(blank=True, null=True)
    civic_education_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    civic_education_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    arabic_language_ca = models.IntegerField(blank=True, null=True)
    arabic_language_exam = models.IntegerField(blank=True, null=True)
    arabic_language_total = models.IntegerField(blank=True, null=True)
    arabic_language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    arabic_language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    tarikh_ca = models.IntegerField(blank=True, null=True)
    tarikh_exam = models.IntegerField(blank=True, null=True)
    tarikh_total = models.IntegerField(blank=True, null=True)
    tarikh_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    tarikh_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)























class AlbumC(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CommerceAlbums(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    albums = models.ForeignKey(AlbumC,
    on_delete=models.CASCADE)

    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Commerce(models.Model):
    name = models.CharField(max_length=50)
    class_of = models.ForeignKey(CommerceAlbums, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, max_length=100)

    TERMS = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third')
    )
    terms = models.CharField(max_length=100, choices=TERMS)
    REMARK = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fail', 'Fail'),
        ('Pass', 'Pass')
    )
    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    english_language_ca = models.IntegerField(blank=True, null=True)
    english_language_exam = models.IntegerField(blank=True, null=True)
    english_language_total = models.IntegerField(blank=True, null=True)
    english_language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    english_language_remark = models.CharField(max_length=100, blank=True, choices=REMARK)

    mathematics_ca = models.IntegerField(blank=True, null=True)
    mathematics_exam = models.IntegerField(blank=True, null=True)
    mathematics_total = models.IntegerField(blank=True, null=True)
    mathematics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    mathematics_remark = models.CharField(max_length=100, blank=True, choices=REMARK)

    economics_ca = models.IntegerField(blank=True, null=True)
    economics_exam = models.IntegerField(blank=True, null=True)
    economics_total = models.IntegerField(blank=True, null=True)
    economics_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    economics_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    accounting_ca = models.IntegerField(blank=True, null=True)
    accounting_exam = models.IntegerField(blank=True, null=True)
    accounting_total = models.IntegerField(blank=True, null=True)
    accounting_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    accounting_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    financial_accounting_ca = models.IntegerField(blank=True, null=True)
    financial_accounting_exam = models.IntegerField(blank=True, null=True)
    financial_accounting_total = models.IntegerField(blank=True, null=True,)
    financial_accounting_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    financial_accounting_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    commerce_ca = models.IntegerField(blank=True, null=True)
    commerce_exam = models.IntegerField(blank=True, null=True,)
    commerce_total = models.IntegerField(blank=True, null=True,)
    commerce_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    commerce_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    language_ca = models.IntegerField(blank=True, null=True)
    language_exam = models.IntegerField(blank=True, null=True,)
    language_total = models.IntegerField(blank=True, null=True,)
    language_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    language_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    civic_education_ca = models.IntegerField(blank=True, null=True)
    civic_education_exam = models.IntegerField(blank=True, null=True,)
    civic_education_total = models.IntegerField(blank=True, null=True,)
    civic_education_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    civic_education_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    computer_ca = models.IntegerField(blank=True, null=True)
    computer_exam = models.IntegerField(blank=True, null=True)
    computer_total = models.IntegerField(blank=True, null=True)
    computer_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    computer_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    data_processing_ca = models.IntegerField(blank=True, null=True)
    data_processing_exam = models.IntegerField(blank=True, null=True,)
    data_processing_total = models.IntegerField(blank=True, null=True,)
    data_processing_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    data_processing_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    religion_ca = models.IntegerField(blank=True, null=True)
    religion_exam = models.IntegerField(blank=True, null=True)
    religion_total = models.IntegerField(blank=True, null=True)
    religion_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    religion_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    tarikh_ca = models.IntegerField(blank=True, null=True)
    tarikh_exam = models.IntegerField(blank=True, null=True,)
    tarikh_total = models.IntegerField(blank=True, null=True,)
    tarikh_grade = models.CharField(max_length=100, null=True, blank=True, choices=GRADE)
    tarikh_remark = models.CharField(max_length=100, null=True, blank=True, choices=REMARK)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name