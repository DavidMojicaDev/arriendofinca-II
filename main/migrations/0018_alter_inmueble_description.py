# Generated by Django 4.2.11 on 2024-04-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_imagenes_inmueble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
