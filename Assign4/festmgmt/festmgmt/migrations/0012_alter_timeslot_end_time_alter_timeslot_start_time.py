# Generated by Django 4.1.7 on 2024-03-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festmgmt', '0011_alter_participant_accomodation_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
