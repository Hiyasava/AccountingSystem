# Generated by Django 3.2.25 on 2024-05-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0003_alter_projects_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='employee_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
