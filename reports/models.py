from django.db import models
from datetime import datetime

# Create your models here.
class Reports(models.Model):

    CHOICES = (
        ('READY', 'Ready'),
        ('NOT READY', 'Not ready')
    )

    entry_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length = 248, null=True)
    type = models.CharField(max_length=256, default='None')
    date = models.DateField(default=datetime.now())

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Reports'

class generatedReports(models.Model):
    name = models.CharField(max_length=256, null=True, default=datetime.now())
    type = models.CharField(max_length=256, null=True)
    date_range = models.CharField(max_length=256, null=True)
    download_link = models.CharField(max_length=256, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'generatedReports'
