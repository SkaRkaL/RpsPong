# Generated by Django 4.2.13 on 2025-01-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0018_player_perfect_win_game_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='win_20_games',
            new_name='win_30_games',
        ),
    ]
