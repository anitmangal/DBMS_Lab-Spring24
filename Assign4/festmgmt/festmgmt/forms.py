from django import forms
from django.db import transaction
from .models import useracc, Student, Organiser, Participant

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = useracc
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'role']

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
    
class ParticipantCreationForm(UserCreationForm):
    is_external = forms.BooleanField(required=False)
    food = forms.CharField(required=True)
    accomodation_building = forms.CharField(required=True)
    accomodation_room = forms.CharField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = Participant
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'collegeName', 'collegeLocation', 'is_external', 'food', 'accomodation_building', 'accomodation_room']
    
    @transaction.atomic  # Ensures data integrity during the creation process
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'participant'  # Assuming you have a role field to distinguish users
        if commit:
            user.save()
            # Create Participant profile
            Participant.objects.create(
                user=user,
                is_external=self.cleaned_data['is_external'],
                food=self.cleaned_data['food'],
                accomodation_building=self.cleaned_data['accomodation_building'],
                accomodation_room=self.cleaned_data['accomodation_room'],
            )
        return user