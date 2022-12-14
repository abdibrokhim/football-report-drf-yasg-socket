# Generated by Django 4.1.1 on 2022-09-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('point', models.PositiveIntegerField(default=0)),
                ('ghost', models.BooleanField(default=False)),
                ('team_1', models.CharField(max_length=254)),
                ('team_2', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('logo', models.ImageField(max_length=254, upload_to='imgs')),
            ],
        ),
    ]
