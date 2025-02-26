# Generated by Django 5.1.4 on 2025-01-29 07:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0056_chatroom_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='from_user',
            field=models.ForeignKey(default=1, limit_choices_to={'role': 'conductor'}, on_delete=django.db.models.deletion.CASCADE, related_name='from_rooms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatroom',
            name='to_user',
            field=models.ForeignKey(default=1, limit_choices_to={'role': 'normal_user'}, on_delete=django.db.models.deletion.CASCADE, related_name='to_rooms', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
