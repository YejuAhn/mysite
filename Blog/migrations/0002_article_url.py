# Generated by Django 3.0.6 on 2020-05-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default='https://www.google.com/'),
        ),
    ]