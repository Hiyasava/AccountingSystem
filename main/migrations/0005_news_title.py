# Generated by Django 5.0.6 on 2024-06-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]