# Generated by Django 4.1.3 on 2023-01-12 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0031_remove_lecture_course_lecture_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.section'),
        ),
    ]
