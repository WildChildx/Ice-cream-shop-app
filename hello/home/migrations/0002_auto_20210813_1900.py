# Generated by Django 3.0.8 on 2021-08-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='number',
        ),
    ]
