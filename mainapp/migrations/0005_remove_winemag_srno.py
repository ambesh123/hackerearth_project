# Generated by Django 2.1.7 on 2019-02-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190217_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winemag',
            name='srno',
        ),
    ]
