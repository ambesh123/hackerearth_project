# Generated by Django 2.1.7 on 2019-02-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_winemag_srno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winemag',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='winemag',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]