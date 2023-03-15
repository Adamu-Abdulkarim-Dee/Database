# Generated by Django 4.1.6 on 2023-03-14 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import jsignature.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondaryAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.CharField(max_length=1000)),
                ('profile_picture', models.FileField(upload_to='image')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=7)),
                ('address_of_student', models.CharField(max_length=100)),
                ('class_Of_student', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(max_length=10)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Christianity', 'Christianity'), ('Atheism', 'Atheism'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Judaism', 'Judaism'), ('Catholicism', 'Catholicism'), ('Rastafari', 'Rastafari'), ('Agnostic', 'Agnostic'), ('Other', 'Other')], max_length=25)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('signature_of_student', jsignature.fields.JSignatureField()),
                ('comment_of_student', models.TextField(blank=True, max_length=50, null=True)),
                ('nationality_of_student', django_countries.fields.CountryField(max_length=2)),
                ('state_of_student', models.CharField(max_length=30)),
                ('local_government_of_student', models.CharField(max_length=50)),
                ('certificate_of_birth_photo', models.ImageField(upload_to='image')),
                ('residential_certificate_photo', models.ImageField(upload_to='image')),
                ('name_of_guardian', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address_of_guardian', models.CharField(max_length=50)),
                ('nationality_of_guardian', django_countries.fields.CountryField(max_length=2)),
                ('state_of_guardian', models.CharField(max_length=30)),
                ('local_government_of_guardian', models.CharField(max_length=50)),
                ('occupation_of_guardian', models.CharField(max_length=50)),
                ('work_address', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=50)),
                ('signature_of_guardian', jsignature.fields.JSignatureField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('year_of_graduation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.secondaryalbum')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Primary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_number', models.CharField(max_length=40)),
                ('profile_picture', models.FileField(upload_to='image')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address_of_student', models.CharField(max_length=50)),
                ('class_Of_student', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(max_length=10)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Christianity', 'Christianity'), ('Atheism', 'Atheism'), ('Hinduism', 'Hinduism'), ('Buddhism', 'Buddhism'), ('Judaism', 'Judaism'), ('Catholicism', 'Catholicism'), ('Rastafari', 'Rastafari'), ('Agnostic', 'Agnostic'), ('Other', 'Other')], max_length=25)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('signature_of_student', jsignature.fields.JSignatureField()),
                ('comment_of_student', models.TextField(blank=True, max_length=50, null=True)),
                ('nationality_of_student', django_countries.fields.CountryField(max_length=2)),
                ('state_of_student', models.CharField(max_length=30)),
                ('local_government_of_student', models.CharField(max_length=50)),
                ('certificate_of_birth_photo', models.ImageField(upload_to='image')),
                ('residential_certificate_photo', models.ImageField(upload_to='image')),
                ('name_of_guardian', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address_of_guardian', models.CharField(max_length=50)),
                ('nationality_of_guardian', django_countries.fields.CountryField(max_length=2)),
                ('state_of_guardian', models.CharField(max_length=50)),
                ('local_government_of_guardian', models.CharField(max_length=50)),
                ('occupation_of_guardian', models.CharField(max_length=50)),
                ('work_address', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=25)),
                ('signature_of_guardian', jsignature.fields.JSignatureField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('year_of_graduation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.primaryalbum')),
            ],
        ),
    ]
