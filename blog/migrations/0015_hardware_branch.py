# Generated by Django 4.2 on 2023-04-27 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.branch'),
        ),
    ]
