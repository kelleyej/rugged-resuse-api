from django.db import models

class Gear(models.Model):
    CATEGORY_CHOICES = [
        ('tents', 'Tents'),
        ('sleeping-bags', 'Sleeping Bags'),
        ('entertainment', 'Entertainment'),
    ]  

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', default='https://media.baamboozle.com/uploads/images/1197896/1677692362_34951_gif-url.gif')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='camping')


    def __str__(self):
        return self.title