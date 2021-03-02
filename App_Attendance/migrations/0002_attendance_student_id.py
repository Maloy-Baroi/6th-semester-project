# Generated by Django 3.1.7 on 2021-03-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Attendance', '0001_initial'),
        ('App_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_in_attendance', to='App_login.studentinfo'),
        ),
    ]
