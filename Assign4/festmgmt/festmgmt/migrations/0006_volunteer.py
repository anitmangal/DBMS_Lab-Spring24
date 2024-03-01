# Generated by Django 4.1.7 on 2024-03-01 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festmgmt', '0005_alter_timeslot_end_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.student')),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
                'unique_together': {('student', 'event')},
            },
        ),
    ]
