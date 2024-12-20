# Generated by Django 5.1.3 on 2024-11-16 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('special', models.CharField(max_length=100)),
                ('place', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
                ('organizer', models.CharField(max_length=50)),
                ('partners', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/avatar/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('second_name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('birth', models.DateField(auto_now_add=True)),
                ('is_organizer', models.BooleanField(default=False, help_text='Я организатор')),
                ('category', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=100)),
                ('github', models.URLField()),
                ('image', models.ImageField(null=True, upload_to='image/event/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Events.event')),
            ],
        ),
    ]
