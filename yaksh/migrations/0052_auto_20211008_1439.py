# Generated by Django 3.1.7 on 2021-10-08 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0051_auto_20211006_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_Premium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Real_Answer_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('attempt_number', models.IntegerField(default='')),
                ('marks_obtained', models.IntegerField(default='')),
                ('percentage', models.FloatField(default='')),
                ('result', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 8, 9, 9, 49, 576369, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 8, 9, 9, 49, 576369, tzinfo=utc)),
        ),
    ]
