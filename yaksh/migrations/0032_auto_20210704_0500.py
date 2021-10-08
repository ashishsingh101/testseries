# Generated by Django 3.1.7 on 2021-07-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0031_auto_20210704_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('bash', 'Bash'), ('c', 'C Language'), ('cpp', 'C++ Language'), ('java', 'Java Language'), ('scilab', 'Scilab'), ('r', 'R'), ('other', 'Other'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], max_length=24),
        ),
    ]
