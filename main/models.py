from django.db import models

class News(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.TextField(null=True)
