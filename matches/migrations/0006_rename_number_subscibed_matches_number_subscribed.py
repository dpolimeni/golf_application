# Generated by Django 4.2.1 on 2023-06-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_matches_number_subscibed_alter_matches_group_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matches',
            old_name='number_subscibed',
            new_name='number_subscribed',
        ),
    ]
