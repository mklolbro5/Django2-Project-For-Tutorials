# Generated by Django 2.0.4 on 2018-04-11 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
