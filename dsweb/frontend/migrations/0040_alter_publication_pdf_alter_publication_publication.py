# Generated by Django 4.1.3 on 2023-01-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0039_publicationcategories_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='PDF',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='Publication',
            field=models.TextField(null=True),
        ),
    ]
