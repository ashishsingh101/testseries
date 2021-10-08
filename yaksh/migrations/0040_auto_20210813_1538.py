# Generated by Django 3.1.12 on 2021-08-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0039_auto_20210811_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcqtestcase',
            name='option_image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(blank=True, choices=[('python', 'Python'), ('bash', 'Bash'), ('c', 'C Language'), ('cpp', 'C++ Language'), ('java', 'Java Language'), ('scilab', 'Scilab'), ('r', 'R'), ('other', 'Other'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], max_length=24, null=True),
        ),
    ]
