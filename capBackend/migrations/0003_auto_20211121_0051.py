# Generated by Django 3.2.9 on 2021-11-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capBackend', '0002_place_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.CharField(default='no image', max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(default='no reviews', max_length=500),
        ),
    ]
