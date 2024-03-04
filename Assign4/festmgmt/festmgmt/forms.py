from django import forms
from django.db import transaction
from .models import useracc, Student, Organiser, Participant, Event_Winner, Event, TimeSlot, Venue

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
            if self.cleaned_data['role']=='participant':
                is_ex = "True"
            else:
                is_ex = "False"
            # Create Participant profile
            Participant.objects.create(
                user=user,
                is_external=is_ex,
                food=self.cleaned_data['food'],
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
        else:
            print("Error")    
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
    
class AddWinnerForm(forms.ModelForm):
    participant_id = forms.ModelChoiceField(queryset=Participant.objects.all(), required=True, widget=forms.TextInput)
    position = forms.ChoiceField(choices=[(x, x) for x in range(1, 4)], required=True)

    class Meta:
        model = Event_Winner
        fields = ['participant_id', 'position']

    def __init__(self, *args, **kwargs):
        self.event_id = kwargs.pop('event_id', None)
        super(AddWinnerForm, self).__init__(*args, **kwargs)
        participants = Participant.objects.exclude(event_winner__event_id=self.event_id)
        self.fields['participant_id'].queryset = participants

    @transaction.atomic
    def save(self, commit=True):
        if commit:
            event = Event.objects.get(event_id=self.event_id)
            event.is_done = True
            event.save()
            Event_Winner.objects.create(
                participant_id=self.cleaned_data['participant_id'],
                event_id=event,
                position=self.cleaned_data['position'],
            )
        else:
            print("Error")

class TimeSlotCreationForm(forms.ModelForm):
    date = forms.DateField(required=True)
    start_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)

    class Meta:
        model = TimeSlot
        fields = ['date', 'start_time', 'end_time']

    @transaction.atomic
    def save(self, commit=True):
        if commit:
            Event.objects.create(
                date=self.cleaned_data['date'],
                start_time=self.cleaned_data['start_time'],
                end_time=self.cleaned_data['end_time'],
            )
        else:
            print("Error")

class VenueCreationForm(forms.ModelForm):
    venue_name = forms.CharField(required=True)
    building = forms.CharField(required=True)
    audio_visual = forms.BooleanField(required=True)
    computer_terminals = forms.BooleanField(required=True)
    capacity = forms.IntegerField(required=True)

    class Meta:
        model = Venue
        fields = ['venue_name', 'building', 'audio_visual', 'computer_terminals', 'capacity']

    @transaction.atomic
    def save(self, commit=True):
        if commit:
            Venue.objects.create(
                venue_name=self.cleaned_data['venue_name'],
                building=self.cleaned_data['building'],
                audio_visual=self.cleaned_data['audio_visual'],
                computer_terminals=self.cleaned_data['computer_terminals'],
                capacity=self.cleaned_data['capacity'],
            )
        else:
            print("Error")

class TimeSlotChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.start_time} to {obj.end_time}"
    
class VenueChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.venue_name

class DateChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj['date']

class EventCreationForm(forms.ModelForm):
    time_slot_id = forms.ModelChoiceField(
        queryset=TimeSlot.objects.all().order_by('date', 'start_time'),
        widget=forms.RadioSelect,
        empty_label=None,
        label="Select Time Slot :"
    )
    venue_name = forms.ModelChoiceField(queryset=Venue.objects.all(), required=True)

    class Meta:
        model = Event
        fields = ['event_name', 'event_type', 'event_description','venue_name', 'time_slot_id']

    @transaction.atomic
    def save(self, commit=True):
        event = super().save(commit=False)
        existing_event = Event.objects.filter(time_slot_id=self.cleaned_data['time_slot_id'], venue_name=self.cleaned_data['venue_name'])
        if existing_event:
            raise forms.ValidationError("The venue is already booked for the selected time slot.")
        if commit:
            event.save()
        return event