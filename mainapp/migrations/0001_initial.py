# Generated by Django 2.1.7 on 2019-02-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_auth',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
