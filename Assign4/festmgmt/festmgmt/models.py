from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

# Add your models here

class useracc(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True)
    phone = PhoneNumberField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=50)    
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
    YEAR_IN_COLLEGE_CHOICES = [(1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth')]
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