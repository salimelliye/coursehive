# Generated by Django 4.1.3 on 2022-12-04 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
    ]