# Generated by Django 3.0.6 on 2020-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('url', models.URLField(default='https://www.google.com/')),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=30)),
                ('text', models.TextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(default='gallery/FitSimplify.jpg', upload_to='gallery')),
            ],
        ),
    ]
