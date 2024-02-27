from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class useracc(AbstractUser, PermissionsMixin): # ??? user is renamed to user accounts
    
    user_id = models.AutoField(primary_key=True) # ??? making the ids an auto field that generates unique number as PK
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True)
    phone = PhoneNumberField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=50)
    address = models.TextField()    
    username = models.CharField(max_length=300, unique=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone', 'dob', 'gender', 'address']
    
class Student(useracc):
    roll_number = models.CharField(max_length=50,primary_key=True)
    dept = models.CharField(max_length=100)
    YEAR_IN_COLLEGE_CHOICES = [1,2,3,4,5]
    year = models.IntegerField(choices=YEAR_IN_COLLEGE_CHOICES)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-roll_number']
    REQUIRED_FIELDS = ['roll_number']
    
