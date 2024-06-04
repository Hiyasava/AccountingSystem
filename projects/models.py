from django.db import models

class Project(models.Model):

    CHOICES = (
        ('READY', 'Ready'),
        ('NOT READY', 'Not ready')
    )

    employee_id = models.CharField(null=True, max_length=50)
    hours = models.IntegerField(null=False)
    projects = models.CharField(null=False, max_length=50)
    state = models.CharField(max_length = 15, choices=CHOICES)
    comment = models.TextField(null=True, max_length=50)
    deadline = models.DateField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.projects

    class Meta:
        verbose_name = 'Проекты'