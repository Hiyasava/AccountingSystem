# Generated by Django 4.2.9 on 2024-05-19 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='img',
            new_name='image',
        ),
    ]
