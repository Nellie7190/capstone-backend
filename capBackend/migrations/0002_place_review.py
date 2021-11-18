# Generated by Django 3.2.9 on 2021-11-14 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('isBlackOwned', models.BooleanField()),
                ('isWomanOwned', models.BooleanField()),
                ('isENMOwned', models.BooleanField()),
                ('isLComOwned', models.BooleanField()),
                ('allowsPets', models.BooleanField()),
                ('hoursOpen', models.CharField(default='0', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isBlackOwned', models.BooleanField(default=False)),
                ('isWomanOwned', models.BooleanField(default=False)),
                ('isENMOwned', models.BooleanField(default=False)),
                ('isLComOwned', models.BooleanField(default=False)),
                ('allowsPets', models.BooleanField(default=False)),
                ('hoursOpen', models.CharField(default='0', max_length=10)),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(default='no reviews', max_length=200)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='capBackend.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='capBackend.user')),
            ],
        ),
    ]
