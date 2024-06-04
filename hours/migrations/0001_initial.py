# Generated by Django 4.2.9 on 2024-03-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(default=1231)),
                ('date', models.DateField(verbose_name='Дата')),
                ('hours', models.IntegerField()),
                ('projects', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Проекты',
            },
        ),
    ]
