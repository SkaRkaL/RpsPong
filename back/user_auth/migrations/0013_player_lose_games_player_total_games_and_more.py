# Generated by Django 4.2.13 on 2025-01-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0012_player_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='lose_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='win_games',
            field=models.IntegerField(default=0),
        ),
    ]
