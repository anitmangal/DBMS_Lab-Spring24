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
    # ????food
    accomodation_building = models.CharField(max_length=100)
    accomodation_room = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ['-participant_id']
    REQUIRED_FIELDS = ['participant_id']

