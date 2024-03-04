from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import admin, messages
from django.shortcuts import get_object_or_404
from .forms import UserCreationForm, StudentCreationForm, OrganiserCreationForm, ParticipantCreationForm, AddWinnerForm, EventCreationForm
from .models import Event, Volunteer, Student, Participant, Participates, useracc, TimeSlot, Venue, Event_Winner
from django.db import transaction
from django.db.models import Q
from django.db.models import CASCADE
from django.db.models import deletion
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from datetime import datetime
from django import forms


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('adminview')
        if request.user.role == 'student':
            return redirect('student_login')
        elif request.user.role == 'organiser':
            return redirect('organiser_login')
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
            return render(request, 'register.html', {'error': 'Invalid form data. Please try again.'})
    return render(request, 'register.html')

@login_required(login_url="student_login")
def student_login_view(request):
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'
    participate = Participates.objects.all()
    participants = Participant.objects.all()
    event_winners = Event_Winner.objects.all()
    
    participant_id_student = -1
    
    curr_username = request.user
    student = Student.objects.get(username=curr_username)
    volunteered_for_events = []
    participated_for_events = []
    declared_winner_events = []
    if student.is_authenticated:
        volunteered_events = Volunteer.objects.filter(student=student)
        for event in volunteered_events:
            volunteered_for_events.append(event.event_id)
        for event in event_winners:
            declared_winner_events.append(event.event_id.event_id)
        # find the participant associated with the user_id of the student
        try:
            curr_participant = Participant.objects.get(user_id=student.user_id)
            participant_id_student = curr_participant.participant_id
            for participated_event in participate:
                if participated_event.participant_id.participant_id == curr_participant.participant_id:                
                    participated_for_events.append(participated_event.event_id.event_id)
        except:
            pass    
        
    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'student_login.html', {'participant_id_student':participant_id_student, 'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type, 'volunteered_for_events': volunteered_for_events, 'participated_for_events': participated_for_events, 'event_winners': event_winners, 'declared_winner_events': declared_winner_events})

def student_participated_events_view(request):
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'
    participate = Participates.objects.all()
    event_winners = Event_Winner.objects.all()
    participant_id_student = -1
    
    curr_username = request.user
    student = Student.objects.get(username=curr_username)
    participated_for_events = []
    declared_winner_events = []
    if student.is_authenticated:
        # find the participant associated with the user_id of the student
        for event in event_winners:
            declared_winner_events.append(event.event_id.event_id)
        try:
            curr_participant = Participant.objects.get(user_id=student.user_id)
            participant_id_student = curr_participant.participant_id
        except:
            curr_participant = None
        for participated_event in participate:
            if participated_event.participant_id.participant_id == curr_participant.participant_id:                
                participated_for_events.append(participated_event.event_id)

    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'student_participated_events.html', {'participant_id_student':participant_id_student, 'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type, 'participated_for_events': participated_for_events, 'event_winners': event_winners, 'declared_winner_events': declared_winner_events})

def student_volunteered_events_view(request):
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'
    
    curr_username = request.user
    student = Student.objects.get(username=curr_username)
    volunteered_for_events = []
    if student.is_authenticated:
        volunteer_objects= Volunteer.objects.filter(student=student)
        for volunteer_object in volunteer_objects:
            volunteered_for_events.append(volunteer_object.event)

    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'student_volunteered_events.html', {'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type, 'volunteered_for_events': volunteered_for_events})

def logout_view(request):
    logout(request)
    # Redirect to a logged-out page or home page
    return redirect('login')

@login_required(login_url='student_login')
@transaction.atomic
def volunteer_event(request, event_id):
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
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
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    user_acc = useracc.objects.get(username=curr_username)
    student = Student.objects.get(username=curr_username)

    if Participates.objects.filter(participant_id = user_acc.user_id, event_id = event.event_id).exists():
        return redirect('student_login')

    if not Participant.objects.filter(user_id=user_acc.user_id).exists():
        participant = Participant(user_id=user_acc.user_id)
        participant.__dict__.update(user_acc.__dict__)
        participant.save()
    else:
        participant = Participant.objects.get(user_id=user_acc.user_id)
    # Save the Participant object
    participates=Participates.objects.create(
        participant_id=participant,
        event_id=event
    )
    return redirect('student_login')

@login_required(login_url='events')
@transaction.atomic
def participate_event(request, event_id):
    if request.user.role != 'participant':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    user_acc = useracc.objects.get(username=curr_username)
    participant = Participant.objects.get(user_id=user_acc.user_id)

    if Participates.objects.filter(participant_id=user_acc.user_id, event_id=event.event_id).exists():
        return redirect('events')

    # Create the Participates object
    Participates.objects.create(
        participant_id=participant,
        event_id=event
    )

    return redirect('events')


@login_required(login_url="organiser_login")
def organiser_login_view(request):
    if request.user.role != 'organiser':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    # Retrieve all events, timeslots, venues, and volunteers from the database
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'

    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        elif search_type == 'volunteer_roll_number':
            events = events.filter(volunteer__student__roll_number__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'organiser_login.html', {'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type})

@login_required(login_url="organiser_login")
def add_winner(request, event_id):
    if request.user.role != 'organiser':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = AddWinnerForm(request.POST, event_id=event.event_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Winner added successfully.')
            return redirect('organiser_login')
        else:
            messages.error(request, 'Invalid Participant ID.')
            return render(request, 'add_winner.html', {'form': form})
    else:
        form = AddWinnerForm(event_id=event.event_id)
    return render(request, 'add_winner.html', {'form': form})

@login_required(login_url="organiser_login")
def create_event_view(request):
    message = None
    if request.method == 'POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('organiser_login')
            except forms.ValidationError as e:
                message = str(e)[2:-2]
    else:
        form = EventCreationForm()
    return render(request, 'create_event.html', {'form': form, 'error_message': message})

@login_required(login_url="organiser_login")
def load_timeslots(request):
    date_str = request.GET.get('date')
    date_id = datetime.strptime(date_str, '%Y-%m-%d').date()
    timeslots = TimeSlot.objects.filter(date=date_id).order_by('start_time')
    html = render_to_string('timeslots_dropdown_list_options.html', {'timeslots': timeslots})
    return HttpResponse(html)

@login_required(login_url="events")
def events_view(request):
    if request.user.role != 'participant':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'
    participate = Participates.objects.all()
    event_winners = Event_Winner.objects.all()

    curr_username = request.user
    participant = Participant.objects.get(username=curr_username)
    participated_for_events = []
    declared_winner_events = []
    if participant.is_authenticated:
        for event in event_winners:
            declared_winner_events.append(event.event_id.event_id)
        for participated_event in participate:
            if participated_event.participant_id.participant_id == participant.participant_id:                
                participated_for_events.append(participated_event.event_id.event_id)


    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'events.html', {'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type, 'participated_for_events': participated_for_events, 'event_winners': event_winners, 'declared_winner_events': declared_winner_events})

@login_required(login_url="events")
def participated_events_view(request):
    if request.user.role != 'participant':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    message = 'No events available.'
    participate = Participates.objects.all()
    event_winners = Event_Winner.objects.all()

    curr_username = request.user
    participant = Participant.objects.get(username=curr_username)
    participated_for_events = []
    declared_winner_events = []
    if participant.is_authenticated:
        for event in event_winners:
            declared_winner_events.append(event.event_id.event_id)
        for participated_event in participate:
            if participated_event.participant_id.participant_id == participant.participant_id:                
                participated_for_events.append(participated_event.event_id)

    query = request.GET.get('search')
    search_type = request.GET.get('search_type')
    if query is not None:
        if search_type == 'event_name':
            events = events.filter(event_name__icontains=query)
        elif search_type == 'event_type':
            events = events.filter(event_type__icontains=query)
        elif search_type == 'event_description':
            events = events.filter(event_description__icontains=query)
        elif search_type == 'venue_name':
            events = events.filter(venue_name__venue_name__icontains=query)
        if not events.exists():
            message = 'No such events!'

    return render(request, 'participated_events.html', {'declared_winner_events': declared_winner_events, 'event_winners': event_winners, 'events': events, 'timeslots': timeslots, 'venues': venues, 'message': message, 'query': query, 'search_type': search_type, 'participated_for_events': participated_for_events})

@login_required(login_url='student_login')
@transaction.atomic
def unparticipate_event(request, event_id):
    if request.user.role != 'student' and request.user.role != 'participant':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    user_acc = useracc.objects.get(username=curr_username)
    # get the participant object
    participant = Participant.objects.get(user_id=user_acc.user_id)
    print(participant.participant_id)
    
    if Participates.objects.filter(participant_id=participant.participant_id, event_id=event.event_id).exists():
        # delete the entry from participates table
        Participates.objects.filter(participant_id=participant, event_id=event).delete()
    
    if user_acc.role == 'participant':
        return redirect('events')
    # if not Participates.objects.filter(participant_id=participant.participant_id).exists():
    #     print('error here')
    #     participant = Participant.objects.filter(user_id=user_acc.user_id)
    #     collector = deletion.Collector(using=participant._state.db)
    #     collector.add([participant])
    #     collector.delete()
    return redirect('student_login')

@login_required(login_url='student_login')
@transaction.atomic
def unvolunteer_student_event(request, event_id):
    if request.user.role != 'student':
        return HttpResponseNotAllowed('You are not allowed to access this page')
    event = Event.objects.get(pk=event_id)
    curr_username = request.user
    student = Student.objects.get(username=curr_username)
    if Volunteer.objects.filter(student=student, event=event).exists():
        print('deleting')
        Volunteer.objects.filter(student=student, event=event).delete()
    return redirect('student_login')