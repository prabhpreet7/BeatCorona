# Generated by Django 3.0.4 on 2020-06-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200607_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='info',
            field=models.CharField(default='No Information Available', max_length=35),
        ),
    ]