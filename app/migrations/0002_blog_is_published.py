# Generated by Django 5.0.2 on 2024-02-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
