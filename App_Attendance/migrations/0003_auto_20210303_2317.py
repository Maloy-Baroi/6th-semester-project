# Generated by Django 3.1.7 on 2021-03-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Attendance', '0002_auto_20210303_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]