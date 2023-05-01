# Generated by Django 4.2 on 2023-04-28 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_organization_details_branches'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentcategory',
            name='description',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hardwaretype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='softwaretype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='softwaretype',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.vendor'),
        ),
    ]
