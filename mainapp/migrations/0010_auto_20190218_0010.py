# Generated by Django 2.1.7 on 2019-02-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20190218_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winemag',
            name='price',
            field=models.FloatField(),
        ),
    ]
