# Generated by Django 4.2 on 2023-06-19 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0003_livestream_body_livestream_date_livestream_is_read'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Livestream',
        ),
    ]
