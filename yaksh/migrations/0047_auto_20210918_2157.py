# Generated by Django 3.1.12 on 2021-09-18 21:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0046_attendance_attendancecourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 18, 21, 57, 35, 413976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2021, 9, 18, 21, 57, 35, 414014, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='AttendanceCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yaksh.attendance')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='yaksh.course')),
            ],
        ),
    ]