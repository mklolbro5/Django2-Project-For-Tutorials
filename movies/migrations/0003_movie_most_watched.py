# Generated by Django 2.2.6 on 2019-11-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='most_watched',
            field=models.BooleanField(default=False),
        ),
    ]
