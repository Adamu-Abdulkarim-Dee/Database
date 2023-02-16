# Generated by Django 4.1.6 on 2023-02-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionprimary',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='sectionprimary',
            name='slug',
        ),
        migrations.AlterField(
            model_name='sectionprimary',
            name='position',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]