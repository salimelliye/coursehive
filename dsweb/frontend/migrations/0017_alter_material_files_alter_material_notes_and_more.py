# Generated by Django 4.1.3 on 2022-12-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_event_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Files',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='material',
            name='Notes',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='material',
            name='Videos',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
