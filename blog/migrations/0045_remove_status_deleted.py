# Generated by Django 4.2 on 2023-05-09 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_status_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='deleted',
        ),
    ]
