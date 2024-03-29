# Generated by Django 4.1.6 on 2023-03-13 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScienceAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.albums')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('terms', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=100)),
                ('english_language_ca', models.IntegerField(blank=True, null=True)),
                ('english_language_exam', models.IntegerField(blank=True, null=True)),
                ('english_language_total', models.IntegerField(blank=True, null=True)),
                ('english_language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('english_language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('mathematics_ca', models.IntegerField(blank=True, null=True)),
                ('mathematics_exam', models.IntegerField(blank=True, null=True)),
                ('mathematics_total', models.IntegerField(blank=True, null=True)),
                ('mathematics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('mathematics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('physics_ca', models.IntegerField(blank=True, null=True)),
                ('physics_exam', models.IntegerField(blank=True, null=True)),
                ('physics_total', models.IntegerField(blank=True, null=True)),
                ('physics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('physics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('biology_ca', models.IntegerField(blank=True, null=True)),
                ('biology_exam', models.IntegerField(blank=True, null=True)),
                ('biology_total', models.IntegerField(blank=True, null=True)),
                ('biology_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('biology_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('chemistry_ca', models.IntegerField(blank=True, null=True)),
                ('chemistry_exam', models.IntegerField(blank=True, null=True)),
                ('chemistry_total', models.IntegerField(blank=True, null=True)),
                ('chemistry_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('chemistry_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('agricultural_science_ca', models.IntegerField(blank=True, null=True)),
                ('agricultural_science_exam', models.IntegerField(blank=True, null=True)),
                ('agricultural_science_total', models.IntegerField(blank=True, null=True)),
                ('agricultural_science_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('agricultural_science_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('computer_ca', models.IntegerField(blank=True, null=True)),
                ('computer_exam', models.IntegerField(blank=True, null=True)),
                ('computer_total', models.IntegerField(blank=True, null=True)),
                ('computer_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('computer_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('data_processing_ca', models.IntegerField(blank=True, null=True)),
                ('data_processing_exam', models.IntegerField(blank=True, null=True)),
                ('data_processing_total', models.IntegerField(blank=True, null=True)),
                ('data_processing_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('data_processing_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('fisheries_ca', models.IntegerField(blank=True, null=True)),
                ('fisheries_exam', models.IntegerField(blank=True, null=True)),
                ('fisheries_total', models.IntegerField(blank=True, null=True)),
                ('fisheries_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('fisheries_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('religion_ca', models.IntegerField(blank=True, null=True)),
                ('religion_exam', models.IntegerField(blank=True, null=True)),
                ('religion_total', models.IntegerField(blank=True, null=True)),
                ('religion_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('religion_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('language_ca', models.IntegerField(blank=True, null=True)),
                ('language_exam', models.IntegerField(blank=True, null=True)),
                ('language_total', models.IntegerField(blank=True, null=True)),
                ('language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('civic_education_ca', models.IntegerField(blank=True, null=True)),
                ('civic_education_exam', models.IntegerField(blank=True, null=True)),
                ('civic_education_total', models.IntegerField(blank=True, null=True)),
                ('civic_education_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('civic_education_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('health_education_ca', models.IntegerField(blank=True, null=True)),
                ('health_education_exam', models.IntegerField(blank=True, null=True)),
                ('health_education_total', models.IntegerField(blank=True, null=True)),
                ('health_education_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('health_education_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('tarikh_ca', models.IntegerField(blank=True, null=True)),
                ('tarikh_exam', models.IntegerField(blank=True, null=True)),
                ('tarikh_total', models.IntegerField(blank=True, null=True)),
                ('tarikh_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('tarikh_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('class_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.sciencealbums')),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Primary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(blank=True, max_length=18, null=True)),
                ('name', models.CharField(max_length=50)),
                ('english_language_ca', models.IntegerField()),
                ('english_language_exam', models.IntegerField()),
                ('english_total', models.IntegerField()),
                ('english_language_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('english_language_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('mathematics_ca', models.IntegerField()),
                ('mathematics_exam', models.IntegerField()),
                ('mathematics_total', models.IntegerField()),
                ('mathematics_grade', models.CharField(max_length=3)),
                ('mathematics_remark', models.CharField(max_length=18)),
                ('computer_ca', models.IntegerField()),
                ('computer_exams', models.IntegerField()),
                ('computer_total', models.IntegerField()),
                ('computer_grade', models.CharField(max_length=3)),
                ('computer_remark', models.CharField(max_length=18)),
                ('science_ca', models.IntegerField()),
                ('science_exam', models.IntegerField()),
                ('science_total', models.IntegerField()),
                ('science_grade', models.CharField(max_length=3)),
                ('science_remark', models.CharField(max_length=18)),
                ('social_studies_ca', models.IntegerField(blank=True, null=True)),
                ('social_studies_exam', models.IntegerField(blank=True, null=True)),
                ('social_studies_total', models.IntegerField(blank=True, null=True)),
                ('social_studies_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('social_studies_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('language_ca', models.IntegerField(blank=True, null=True)),
                ('language_exam', models.IntegerField(blank=True, null=True)),
                ('language_total', models.IntegerField(blank=True, null=True)),
                ('language_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('language_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('physical_education_ca', models.IntegerField(blank=True, null=True)),
                ('physical_education_exam', models.IntegerField(blank=True, null=True)),
                ('physical_education_total', models.IntegerField(blank=True, null=True)),
                ('physical_education_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('physical_education_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('history_ca', models.IntegerField(blank=True, null=True)),
                ('history_exam', models.IntegerField(blank=True, null=True)),
                ('history_total', models.IntegerField(blank=True, null=True)),
                ('history_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('history_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('fiqh_ca', models.IntegerField(blank=True, null=True)),
                ('fiqh_exam', models.IntegerField(blank=True, null=True)),
                ('fiqh_total', models.IntegerField(blank=True, null=True)),
                ('fiqh_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('fiqh_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('tawheed_ca', models.IntegerField(blank=True, null=True)),
                ('tawheed_exam', models.IntegerField(blank=True, null=True)),
                ('tawheed_total', models.IntegerField(blank=True, null=True)),
                ('tawheed_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('tawheed_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('arabic_language_ca', models.IntegerField(blank=True, null=True)),
                ('arabic_language_exam', models.IntegerField(blank=True, null=True)),
                ('arabic_language_total', models.IntegerField(blank=True, null=True)),
                ('arabic_language_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('arabic_language_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('quran_ca', models.IntegerField(blank=True, null=True)),
                ('quran_exam', models.IntegerField(blank=True, null=True)),
                ('quran_total', models.IntegerField(blank=True, null=True)),
                ('quran_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('quran_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('tahfidz_ca', models.IntegerField(blank=True, null=True)),
                ('tahfidz_exam', models.IntegerField(blank=True, null=True)),
                ('tahfidz_total', models.IntegerField(blank=True, null=True)),
                ('tahfidz_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('tahfidz_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('agriculture_ca', models.IntegerField(blank=True, null=True)),
                ('agriculture_exam', models.IntegerField(blank=True, null=True)),
                ('agriculture_total', models.IntegerField(blank=True, null=True)),
                ('agriculture_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('agriculture_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('civic_education_ca', models.IntegerField(blank=True, null=True)),
                ('civic_education_exam', models.IntegerField(blank=True, null=True)),
                ('civic_education_total', models.IntegerField(blank=True, null=True)),
                ('civic_education_grade', models.CharField(blank=True, max_length=3, null=True)),
                ('civic_education_remark', models.CharField(blank=True, max_length=18, null=True)),
                ('terms', models.CharField(choices=[('First', 'First'), ('Second', 'second'), ('Third', 'Third')], max_length=100)),
                ('position', models.CharField(blank=True, max_length=10, null=True)),
                ('year', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('class_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.primaryresult')),
            ],
        ),
        migrations.CreateModel(
            name='CommerceAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.albumc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('terms', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=100)),
                ('english_language_ca', models.IntegerField(blank=True, null=True)),
                ('english_language_exam', models.IntegerField(blank=True, null=True)),
                ('english_language_total', models.IntegerField(blank=True, null=True)),
                ('english_language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('english_language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100)),
                ('mathematics_ca', models.IntegerField(blank=True, null=True)),
                ('mathematics_exam', models.IntegerField(blank=True, null=True)),
                ('mathematics_total', models.IntegerField(blank=True, null=True)),
                ('mathematics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('mathematics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100)),
                ('economics_ca', models.IntegerField(blank=True, null=True)),
                ('economics_exam', models.IntegerField(blank=True, null=True)),
                ('economics_total', models.IntegerField(blank=True, null=True)),
                ('economics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('economics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('accounting_ca', models.IntegerField(blank=True, null=True)),
                ('accounting_exam', models.IntegerField(blank=True, null=True)),
                ('accounting_total', models.IntegerField(blank=True, null=True)),
                ('accounting_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('accounting_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('financial_accounting_ca', models.IntegerField(blank=True, null=True)),
                ('financial_accounting_exam', models.IntegerField(blank=True, null=True)),
                ('financial_accounting_total', models.IntegerField(blank=True, null=True)),
                ('financial_accounting_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('financial_accounting_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('commerce_ca', models.IntegerField(blank=True, null=True)),
                ('commerce_exam', models.IntegerField(blank=True, null=True)),
                ('commerce_total', models.IntegerField(blank=True, null=True)),
                ('commerce_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('commerce_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('language_ca', models.IntegerField(blank=True, null=True)),
                ('language_exam', models.IntegerField(blank=True, null=True)),
                ('language_total', models.IntegerField(blank=True, null=True)),
                ('language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('civic_education_ca', models.IntegerField(blank=True, null=True)),
                ('civic_education_exam', models.IntegerField(blank=True, null=True)),
                ('civic_education_total', models.IntegerField(blank=True, null=True)),
                ('civic_education_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('civic_education_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('computer_ca', models.IntegerField(blank=True, null=True)),
                ('computer_exam', models.IntegerField(blank=True, null=True)),
                ('computer_total', models.IntegerField(blank=True, null=True)),
                ('computer_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('computer_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('data_processing_ca', models.IntegerField(blank=True, null=True)),
                ('data_processing_exam', models.IntegerField(blank=True, null=True)),
                ('data_processing_total', models.IntegerField(blank=True, null=True)),
                ('data_processing_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('data_processing_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('religion_ca', models.IntegerField(blank=True, null=True)),
                ('religion_exam', models.IntegerField(blank=True, null=True)),
                ('religion_total', models.IntegerField(blank=True, null=True)),
                ('religion_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('religion_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('tarikh_ca', models.IntegerField(blank=True, null=True)),
                ('tarikh_exam', models.IntegerField(blank=True, null=True)),
                ('tarikh_total', models.IntegerField(blank=True, null=True)),
                ('tarikh_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('tarikh_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('class_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.commercealbums')),
            ],
        ),
        migrations.CreateModel(
            name='ArtAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.albuma')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('terms', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], max_length=100)),
                ('english_language_ca', models.IntegerField(blank=True, null=True)),
                ('english_language_exam', models.IntegerField(blank=True, null=True)),
                ('english_language_total', models.IntegerField(blank=True, null=True)),
                ('english_language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('english_language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('mathematics_ca', models.IntegerField(blank=True, null=True)),
                ('mathematics_exam', models.IntegerField(blank=True, null=True)),
                ('mathematics_total', models.IntegerField(blank=True, null=True)),
                ('mathematics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('mathematics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('government_ca', models.IntegerField(blank=True, null=True)),
                ('government_exam', models.IntegerField(blank=True, null=True)),
                ('government_total', models.IntegerField(blank=True, null=True)),
                ('government_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('government_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('history_ca', models.IntegerField(blank=True, null=True)),
                ('history_exam', models.IntegerField(blank=True, null=True)),
                ('history_total', models.IntegerField(blank=True, null=True)),
                ('history_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('history_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('economics_ca', models.IntegerField(blank=True, null=True)),
                ('economics_exam', models.IntegerField(blank=True, null=True)),
                ('economics_total', models.IntegerField(blank=True, null=True)),
                ('economics_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('economics_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('literature_ca', models.IntegerField(blank=True, null=True)),
                ('literature_exam', models.IntegerField(blank=True, null=True)),
                ('literature_total', models.IntegerField(blank=True, null=True)),
                ('literature_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('literature_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('computer_ca', models.IntegerField(blank=True, null=True)),
                ('computer_exam', models.IntegerField(blank=True, null=True)),
                ('computer_total', models.IntegerField(blank=True, null=True)),
                ('computer_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('computer_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('data_processing_ca', models.IntegerField(blank=True, null=True)),
                ('data_processing_exam', models.IntegerField(blank=True, null=True)),
                ('data_processing_total', models.IntegerField(blank=True, null=True)),
                ('data_processing_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('data_processing_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('religion_ca', models.IntegerField(blank=True, null=True)),
                ('religion_exam', models.IntegerField(blank=True, null=True)),
                ('religion_total', models.IntegerField(blank=True, null=True)),
                ('religion_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('religion_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('language_ca', models.IntegerField(blank=True, null=True)),
                ('language_exam', models.IntegerField(blank=True, null=True)),
                ('language_total', models.IntegerField(blank=True, null=True)),
                ('language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('civic_education_ca', models.IntegerField(blank=True, null=True)),
                ('civic_education_exam', models.IntegerField(blank=True, null=True)),
                ('civic_education_total', models.IntegerField(blank=True, null=True)),
                ('civic_education_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('civic_education_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('arabic_language_ca', models.IntegerField(blank=True, null=True)),
                ('arabic_language_exam', models.IntegerField(blank=True, null=True)),
                ('arabic_language_total', models.IntegerField(blank=True, null=True)),
                ('arabic_language_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('arabic_language_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('tarikh_ca', models.IntegerField(blank=True, null=True)),
                ('tarikh_exam', models.IntegerField(blank=True, null=True)),
                ('tarikh_total', models.IntegerField(blank=True, null=True)),
                ('tarikh_grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True)),
                ('tarikh_remark', models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Fail', 'Fail'), ('Pass', 'Pass')], max_length=100, null=True)),
                ('class_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.artalbums')),
            ],
        ),
    ]
