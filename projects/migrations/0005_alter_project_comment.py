# Generated by Django 4.2.9 on 2024-05-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
