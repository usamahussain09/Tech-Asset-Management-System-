# Generated by Django 4.2 on 2023-05-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0065_asset_software_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='hardware_value',
            new_name='dashboard_value',
        ),
    ]
