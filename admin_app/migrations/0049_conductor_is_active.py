# Generated by Django 5.1.4 on 2025-01-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0048_conductor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
