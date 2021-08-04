# Generated by Django 3.2.6 on 2021-08-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customers_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Gender Customer'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]