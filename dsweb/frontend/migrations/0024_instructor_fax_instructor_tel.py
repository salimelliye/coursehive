# Generated by Django 4.1.3 on 2023-01-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0023_instructor_githuburl'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='Fax',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='Tel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
