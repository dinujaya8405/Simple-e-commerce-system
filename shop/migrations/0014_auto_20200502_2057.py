# Generated by Django 3.0.2 on 2020-05-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200502_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='', max_length=2000),
        ),
    ]
