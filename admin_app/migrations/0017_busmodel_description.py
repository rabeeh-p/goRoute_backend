# Generated by Django 5.1.4 on 2025-01-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0016_busmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='busmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
