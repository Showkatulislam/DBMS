# Generated by Django 3.1.6 on 2021-06-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Chittagong', 'SATAKNIA'), ('Chittagong', 'ANOWARA'), ('Chittagong', 'BOALKHALI'), ('Chittagong', 'CHANDANAISH'), ('Chittagong', 'HATHAZARI'), ('Chittagong', 'MIRSHARAI'), ('Chittagong', 'PATIYA'), ('Chittagong', 'RANGUNIA'), ('Chittagong', 'SANDWIP'), ('Chittagong', 'BOALKHAL')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LF', 'Lower Food'), ('HF', 'Higher Food'), ('SF', 'Special Food'), ('WF', 'Weekly Food')], max_length=2),
        ),
    ]
