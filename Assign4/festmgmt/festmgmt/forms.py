from django import forms
from django.db import transaction
from .models import useracc, Student, Organiser, Participant
import random

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = useracc
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'role']

   
class ParticipantCreationForm(UserCreationForm):
    is_external = forms.BooleanField(required=False)
    food = forms.CharField(required=False)
    accomodation_building = forms.CharField(required=False)
    accomodation_room = forms.CharField(required=False)
    
    class Meta(UserCreationForm.Meta):
        model = Participant
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'is_external', 'food', 'accomodation_building', 'accomodation_room']
    

    @transaction.atomic  # Ensures data integrity during the creation process
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'participant'  # Assuming you have a role field to distinguish users
        if commit:
            user.save()
            hallList = ['LBS', 'VS', 'LLR', 'Nehru', 'Patel', 'Azad']
            if self.cleaned_data['role']=='participant':
                is_ex = "True"
            else:
                is_ex = "False"
            # Create Participant profile
            Participant.objects.create(
                user=user,
                is_external=is_ex,
                food=random.choice(hallList),
                accomodation_building=random.choice(hallList),
                accomodation_room=random.choice(hallList),
            )
        return user

class StudentCreationForm(UserCreationForm):
    roll_number = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    year = forms.ChoiceField(choices=Student.YEAR_IN_COLLEGE_CHOICES, required=True)
    
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'roll_number', 'dept', 'year']

    @transaction.atomic  # Ensures data integrity during the creation process
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'  # Assuming you have a role field to distinguish users
        if commit:
            user.save()
            # Create Student profile
            Student.objects.create(
                user=user,
                roll_number=self.cleaned_data['roll_number'],
                dept=self.cleaned_data['dept'],
                year=self.cleaned_data['year'],
            )
        return user

class OrganiserCreationForm(UserCreationForm):
    position_of_responsibility = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = Organiser
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'position_of_responsibility']

    @transaction.atomic  # Ensures data integrity during the creation process
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'organiser'  # Assuming you have a role field to distinguish users
        if commit:
            user.save()
            # Create Organiser profile
            Organiser.objects.create(
                user=user,
                position_of_responsibility=self.cleaned_data['position_of_responsibility'],
            )
        return user