from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, StudentCreationForm, OrganiserCreationForm, ParticipantCreationForm
from .models import Event, TimeSlot, Venue

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'student':
                return redirect('student_login')
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
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()
            return redirect('login')  # Redirect to login page after successful account creation
        else:
            print(form.errors)
    return render(request, 'register.html')

@login_required(login_url = "student_login")
def student_login_view(request):
    # Retrieve all events from the database
    events = Event.objects.all()
    timeslots = TimeSlot.objects.all()
    venues = Venue.objects.all()
    return render(request, 'student_login.html', {'events': events, 'timeslots': timeslots, 'venues': venues})

# ???? need to add logout

def events_view(request):
    return render(request, 'events.html')