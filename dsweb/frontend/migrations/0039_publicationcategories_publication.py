# Generated by Django 4.1.3 on 2023-01-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0038_remove_instructor_fax_instructor_officehours'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Publication', models.TextField()),
                ('PDF', models.FileField(upload_to='')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.publicationcategories')),
            ],
        ),
    ]
