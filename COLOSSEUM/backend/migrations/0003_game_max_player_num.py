# Generated by Django 2.0.2 on 2018-07-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180718_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='max_player_num',
            field=models.IntegerField(default=2),
        ),
    ]