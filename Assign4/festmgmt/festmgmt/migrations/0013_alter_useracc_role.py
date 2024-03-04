# Generated by Django 4.1.7 on 2024-03-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festmgmt', '0012_alter_timeslot_end_time_alter_timeslot_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracc',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('participant', 'Participant'), ('organizer', 'Organizer')], default='admin', max_length=40, verbose_name='Role'),
        ),
    ]
