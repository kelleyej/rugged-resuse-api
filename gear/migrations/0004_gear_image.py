# Generated by Django 5.1.1 on 2024-10-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0003_remove_gear_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='image',
            field=models.ImageField(default='https://media.baamboozle.com/uploads/images/1197896/1677692362_34951_gif-url.gif', upload_to='images/'),
        ),
    ]
