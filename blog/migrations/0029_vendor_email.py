# Generated by Django 4.2 on 2023-05-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_alter_vendor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
    ]
