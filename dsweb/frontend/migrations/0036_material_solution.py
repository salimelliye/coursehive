# Generated by Django 4.1.3 on 2023-01-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0035_rename_files_material_javafiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='Solution',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Solution Keys'),
        ),
    ]