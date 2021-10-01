# Generated by Django 3.2.7 on 2021-09-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporates', '0006_auto_20210930_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='governance',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='social',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
