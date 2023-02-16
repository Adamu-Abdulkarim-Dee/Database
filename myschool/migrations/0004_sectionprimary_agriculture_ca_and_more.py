# Generated by Django 4.1.6 on 2023-02-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0003_rename_position_sectionprimary_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionprimary',
            name='agriculture_ca',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='agriculture_exam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='agriculture_grade',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='agriculture_remark',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='agriculture_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='civic_education_ca',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='civic_education_exam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='civic_education_grade',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='civic_education_remark',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='sectionprimary',
            name='civic_education_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
