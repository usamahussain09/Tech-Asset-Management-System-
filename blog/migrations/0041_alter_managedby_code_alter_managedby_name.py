# Generated by Django 4.2 on 2023-05-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_remove_managedby_addtobranch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managedby',
            name='code',
            field=models.CharField(max_length=20, null=True, verbose_name='Dept_Code'),
        ),
        migrations.AlterField(
            model_name='managedby',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Department Name'),
        ),
    ]
