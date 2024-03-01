from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class useracc(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True)
    phone = PhoneNumberField(unique=True)
    dob = models.DateField(null=True, blank=True)  # Allow null values here
    gender = models.CharField(max_length=50, null=True, blank=True)  # Allow null values here
    username = models.CharField(max_length=300, unique=True)
    collegeName = models.CharField(max_length=300)
    collegeLocation = models.CharField(max_length=300)
    
    ROLES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('participant', 'Participant'),
        ('organizer', 'Organizer'),
    ]
    role = models.CharField("Role", max_length=40, choices=ROLES, default='participant', blank = False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

class Student(useracc):
    roll_number = models.CharField(max_length=50,primary_key=True)
    dept = models.CharField(max_length=100)
    YEAR_IN_COLLEGE_CHOICES = [(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Fifth Year')]
    year = models.IntegerField(choices=YEAR_IN_COLLEGE_CHOICES)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-roll_number']
    REQUIRED_FIELDS = ['roll_number']

class Organiser(useracc):
    organiser_id = models.AutoField(primary_key=True)
    position_of_responsibility = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Organiser'
        verbose_name_plural = 'Organisers'
        ordering = ['-organiser_id']
    REQUIRED_FIELDS = ['organiser_id']

class Participant(useracc):
    participant_id = models.AutoField(primary_key=True)
    is_external = models.BooleanField(default=False)
    food = models.CharField(max_length=100)
    accomodation_building = models.CharField(max_length=100)
    accomodation_room = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ['-participant_id']
    REQUIRED_FIELDS = ['participant_id']

class Admin(useracc):
    admin_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        ordering = ['-admin_id']
    REQUIRED_FIELDS = ['admin_id']
    
class TimeSlot(models.Model):
    time_slot_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True) # Allow null values here ????  check other places too
    class Meta:
        verbose_name = 'TimeSlot'
        verbose_name_plural = 'TimeSlots'
        ordering = ['-time_slot_id']
    REQUIRED_FIELDS = ['time_slot_id', 'date', 'start_time']

class Venue(models.Model):
    venue_name = models.CharField(max_length=300, primary_key=True)
    building = models.CharField(max_length=300)
    audio_visual = models.BooleanField(default=False) # ???? kept it as boolean field
    computer_terminals = models.BooleanField(default=False) # ???? kept it as boolean field
    capacity = models.IntegerField() # added capacity field
    class Meta:
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'
        ordering = ['-venue_name']
    REQUIRED_FIELDS = ['venue_name', 'building', 'audio_visual', 'computer_terminals', 'capacity']
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=300)
    event_type = models.CharField(max_length=300)
    event_description = models.TextField()
    
    time_slot_id = models.IntegerField(default=0)
        
    venue_name = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-event_id']
    
    time_slot_id = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    venue_name = models.ForeignKey(Venue, on_delete=models.CASCADE)
    REQUIRED_FIELDS = ['event_id', 'event_name', 'time_slot_id', 'venue_name']
    
class Volunteer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'
        unique_together = ('student', 'event')