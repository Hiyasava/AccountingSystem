# Generated by Django 4.2.9 on 2024-05-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='comment',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
