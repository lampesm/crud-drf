# Generated by Django 4.0.4 on 2022-04-17 19:15

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['imdb_score']},
        ),
        migrations.AlterModelManagers(
            name='movie',
            managers=[
                ('custom_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]