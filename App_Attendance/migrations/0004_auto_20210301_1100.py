# Generated by Django 3.1.7 on 2021-03-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Attendance', '0003_auto_20210301_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(max_length=2),
        ),
    ]