# Generated by Django 4.2.1 on 2023-06-09 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_irons_ironownership'),
        ('matches', '0002_matches_group_size_matches_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.clubprofile'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AddConstraint(
            model_name='matches',
            constraint=models.UniqueConstraint(fields=('date', 'club'), name='Unique datetime-Club for each match'),
        ),
    ]
