# Generated by Django 4.2.1 on 2023-05-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_playerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprofile',
            name='address',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='surname',
            field=models.CharField(max_length=64),
        ),
    ]
