# Generated by Django 4.1.3 on 2023-01-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0021_remove_student_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='Cv',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]