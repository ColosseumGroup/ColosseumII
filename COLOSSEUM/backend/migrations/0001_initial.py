# Generated by Django 2.0.2 on 2018-02-21 02:56

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'OnGoing'), ('1', 'Finished'), ('2', 'ErrrorUnfinished')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=32)),
                ('game_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong_to_game_id', models.IntegerField(default=0)),
                ('scores', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong_to_game_id', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('step_taken', models.IntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_status', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('real_name', models.CharField(blank=True, max_length=32, null=True)),
                ('blog', models.URLField(blank=True, null=True)),
                ('mood', models.CharField(blank=True, max_length=256, null=True)),
                ('github', models.CharField(blank=True, max_length=64, null=True)),
                ('school', models.CharField(blank=True, max_length=64, null=True)),
                ('major', models.CharField(blank=True, max_length=64, null=True)),
                ('submission_number', models.IntegerField(default=0)),
                ('win_number', models.IntegerField(default=0)),
                ('games', models.ManyToManyField(to='backend.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.GameType'),
        ),
    ]
