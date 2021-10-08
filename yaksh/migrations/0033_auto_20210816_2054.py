# Generated by Django 3.1.12 on 2021-08-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0032_auto_20210704_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='negative_marking',
            field=models.CharField(choices=[('Tr', 'True'), ('Fl', 'False')], default='Tr', max_length=2),
        ),
        migrations.AddField(
            model_name='quiz',
            name='negative_score',
            field=models.CharField(max_length=1, null=True),
        ),
    ]