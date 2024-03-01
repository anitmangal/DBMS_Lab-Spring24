from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.shortcuts import get_object_or_404
from .forms import UserCreationForm, StudentCreationForm, OrganiserCreationForm, ParticipantCreationForm
from .models import Event, Volunteer, Student, Participant, Participates, useracc, TimeSlot, Venue
from django.db import transaction


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminview')
        return redirect('events')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('adminview')
            if user.role == 'student':
                return redirect('student_login')
            elif user.role == 'organiser':
                return redirect('organiser_login')
            return redirect('events')  # Redirect to home page after successful login
        else:
            # Display error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        role = request.POST.get('role', 'student')  # Get the role from POST data, default to 'student'
        if role == 'student':
            form = StudentCreationForm(request.POST)
        elif role == 'organiser':
            form = OrganiserCreationForm(request.POST)
        else:
            form = ParticipantCreationForm(request.POST)  # Default form

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after successful account creation
        else:
            print(form.errors)
    return render(request, 'register.html')

@login_required(login_url="student_login")
def student_login_view(request):
    events = Event.objects.all()
    participate = Participates.objects.all()
    
    curr_username = request.user
    student = Student.objects.get(username=curr_username)
    volunteered_for_events = []
    participated_for_events = []
    if student.is_authenticated:
        volunteered_events = Volunteer.objects.filter(student=student)
        for event in volunteered_events:
            volunteered_for_events.append(event.event_id)
        # find the participant associated with the user_id of the student
        try:
            curr_participant = Participant.objects.get(user_id=student.user_id)
            for participated_event in participate:
                if participated_event.participant_id.participant_id == curr_participant.participant_id:                
                    participated_for_events.append(participated_event.event_id.event_id)
                    print(participated_event.event_id.event_id)
        except:
            pass    
    return render(request, 'student_login.html', {'events': events, 'volunteered_for_events': volunteered_for_events, 'participated_for_events': participated_for_events})
# ???? need to add logout

@login_required(login_url='student_login')
@transaction.atomic
def volunteer_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    #find the student object
    student = Student.objects.get(username=curr_username)
    if Volunteer.objects.filter(student = student, event = event).exists():
        return redirect('student_login')  # Redirect to the student dashboard    
    Volunteer.objects.create(student = student, event = event)
    return redirect('student_login')

@login_required(login_url='student_login')
@transaction.atomic
def participate_student_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    user_acc = useracc.objects.get(username=curr_username)
    student = Student.objects.get(username=curr_username)

    if Participates.objects.filter(participant_id = user_acc.user_id, event_id = event.event_id).exists():
        return redirect('student_login')
    participant = Participant(user_id=user_acc.user_id)
    participant.__dict__.update(user_acc.__dict__)
    participant.save()
    # Save the Participant object
    Participates.objects.create(
        participant_id=participant,
        event_id=event
    )
    # Save the Participates object
    return redirect('student_login')

@login_required(login_url="organiser_login")
def organiser_login_view(request):
    # Retrieve all events, timeslots, venues, and volunteers from the database
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    # volunteers = Volunteer.objects.all()
    return render(request, 'organiser_login.html', {'events': events, 'timeslots': timeslots, 'venues': venues})

def events_view(request):
    return render(request, 'events.html')
