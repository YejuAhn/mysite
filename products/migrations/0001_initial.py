# Generated by Django 3.0.6 on 2020-06-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField()),
                ('featured', models.BooleanField(default=True)),
                ('image', models.ImageField(default='gallery/FitSimplify.jpg', upload_to='gallery')),
                ('url', models.URLField(default='https://www.google.com/')),
            ],
        ),
    ]
