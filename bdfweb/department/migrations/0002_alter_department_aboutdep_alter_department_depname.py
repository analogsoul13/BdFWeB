# Generated by Django 5.0.6 on 2024-07-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='aboutdep',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='department',
            name='depname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
