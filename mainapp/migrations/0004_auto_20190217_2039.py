# Generated by Django 2.1.7 on 2019-02-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_winemag_srno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winemag',
            name='points',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='winemag',
            name='price',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='winemag',
            name='srno',
            field=models.TextField(null=True),
        ),
    ]