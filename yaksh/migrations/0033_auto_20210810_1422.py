# Generated by Django 3.1.12 on 2021-08-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0032_auto_20210704_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='negative_marks',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.FloatField(default=3.0),
        ),
    ]