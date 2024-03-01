# Generated by Django 4.1.7 on 2024-02-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=300)),
                ('event_type', models.CharField(max_length=300)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue_name', models.CharField(max_length=300)),
                ('building', models.CharField(max_length=300)),
                ('audio_visual', models.BooleanField(default=False)),
                ('computer_terminals', models.BooleanField(default=False)),
                ('capacity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-event_id'],
            },
        ),
    ]