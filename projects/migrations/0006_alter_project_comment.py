# Generated by Django 3.2.25 on 2024-05-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_eemployee_id_project_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]