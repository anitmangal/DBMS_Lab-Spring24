# Generated by Django 4.1.7 on 2024-03-04 07:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='useracc',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=300, unique=True)),
                ('collegeName', models.CharField(max_length=300)),
                ('collegeLocation', models.CharField(max_length=300)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('participant', 'Participant'), ('organizer', 'Organizer')], default='admin', max_length=40, verbose_name='Role')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('time_slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'TimeSlot',
                'verbose_name_plural': 'TimeSlots',
                'ordering': ['-time_slot_id'],
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_name', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('building', models.CharField(max_length=300)),
                ('audio_visual', models.BooleanField(default=False)),
                ('computer_terminals', models.BooleanField(default=False)),
                ('capacity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
                'ordering': ['-venue_name'],
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('useracc_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
                'ordering': ['-admin_id'],
            },
            bases=('festmgmt.useracc',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('useracc_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('organiser_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_of_responsibility', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Organiser',
                'verbose_name_plural': 'Organisers',
                'ordering': ['-organiser_id'],
            },
            bases=('festmgmt.useracc',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('useracc_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('participant_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_external', models.BooleanField(default=False)),
                ('food', models.CharField(blank=True, max_length=100, null=True)),
                ('accomodation_building', models.CharField(blank=True, max_length=100, null=True)),
                ('accomodation_room', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
                'ordering': ['-participant_id'],
            },
            bases=('festmgmt.useracc',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('useracc_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('roll_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dept', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')])),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'ordering': ['-roll_number'],
            },
            bases=('festmgmt.useracc',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=300)),
                ('event_type', models.CharField(max_length=300)),
                ('event_description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
                ('time_slot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.timeslot')),
                ('venue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.venue')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-event_id'],
            },
        ),
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
        migrations.CreateModel(
            name='Participates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.event')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.participant')),
            ],
            options={
                'verbose_name': 'Participates',
                'verbose_name_plural': 'Participate',
                'unique_together': {('participant_id', 'event_id')},
            },
        ),
        migrations.CreateModel(
            name='Event_Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.event')),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='festmgmt.participant')),
            ],
            options={
                'verbose_name': 'Event_Winner',
                'verbose_name_plural': 'Event_Winners',
                'unique_together': {('event_id', 'participant_id')},
            },
        ),
    ]
