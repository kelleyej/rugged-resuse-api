# Generated by Django 5.1.1 on 2024-10-04 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0002_rename_name_gear_title_gear_category_gear_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='image',
        ),
    ]
