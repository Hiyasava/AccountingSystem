# Generated by Django 5.0.6 on 2024-06-12 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_alter_generatedreports_name_alter_reports_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedreports',
            name='name',
            field=models.CharField(default=datetime.datetime(2024, 6, 12, 15, 24, 41, 790437), max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 12, 15, 24, 41, 790222)),
        ),
    ]
