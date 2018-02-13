# Generated by Django 2.0.2 on 2018-02-10 03:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('admin_type', models.CharField(default='Regular User', max_length=32)),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.User')),
            ],
        ),
    ]
