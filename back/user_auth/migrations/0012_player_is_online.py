# Generated by Django 4.2.13 on 2025-01-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0011_player_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
