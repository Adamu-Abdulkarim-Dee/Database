# Generated by Django 4.1.6 on 2023-02-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0008_alter_sectionprimary_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='complaints')),
                ('school_name', models.CharField(max_length=70)),
            ],
        ),
    ]
