# Generated by Django 3.0.6 on 2020-05-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200514_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='gallery/FitSimplify.jpg', upload_to='gallery'),
        ),
    ]