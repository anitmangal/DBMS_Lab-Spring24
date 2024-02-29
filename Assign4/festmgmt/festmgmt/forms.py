from django import forms
from django.db import transaction
from .models import useracc, Student, Organiser

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = useracc
        fields = ['username', 'password', 'name', 'email', 'phone', 'dob', 'gender', 'role']

class StudentCreationForm(UserCreationForm):
    # Add additional fields if necessary, for example:
    roll_number = forms.CharField(required=True)
    dept = forms.CharField(required=True)
    year = forms.ChoiceField(choices=Student.YEAR_IN_COLLEGE_CHOICES, required=True)
    
    class Meta(UserCreationForm.Meta):
        model = useracc
        fields = ['username', 'name', 'email', 'phone', 'dob', 'gender', 'roll_number', 'dept', 'year']

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
        model = useracc
        fields = ['username', 'password', 'name', 'email', 'phone', 'role', 'position_of_responsibility']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'organizer'
        if commit:
            user.save()
            Organiser.objects.create(
                user=user,
                position_of_responsibility=self.cleaned_data['position_of_responsibility'],
            )
        return user
