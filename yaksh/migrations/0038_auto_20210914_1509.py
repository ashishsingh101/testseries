# Generated by Django 3.1.12 on 2021-09-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0037_auto_20210818_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='negative_marks',
            field=models.IntegerField(default=-1.0),
        ),
    ]
