from django.db import models

class Projects(models.Model):
    employee_id = models.CharField(null=True, max_length=50)
    date = models.DateField('Дата')
    hours = models.IntegerField(null=False)
    projects = models.CharField(null=False, max_length=50, default = 'None')
    
    def __str__(self) -> str:
        return self.projects

    class Meta:
        verbose_name = 'Проекты'