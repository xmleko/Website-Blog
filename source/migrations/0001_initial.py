# Generated by Django 5.0.6 on 2024-07-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('difficult_level', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('ingredients', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=400)),
            ],
        ),
    ]
