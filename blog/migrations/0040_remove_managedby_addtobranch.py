# Generated by Django 4.2 on 2023-05-01 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_managedby_addtobranch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managedby',
            name='addtobranch',
        ),
    ]
