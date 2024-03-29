# Generated by Django 4.0.3 on 2022-11-13 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=300)),
                ('deppic', models.FileField(null=True, upload_to='')),
                ('deppin', models.CharField(max_length=6, null=True)),
                ('depidpic', models.FileField(null=True, upload_to='')),
                ('aboutdep', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=20)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('adminremark', models.CharField(max_length=500)),
                ('updationdate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
