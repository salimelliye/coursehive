# Generated by Django 4.1.3 on 2022-12-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_section_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='About',
            field=models.TextField(null=True),
        ),
    ]
