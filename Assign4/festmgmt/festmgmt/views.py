from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, StudentCreationForm, OrganiserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('events')  # Redirect to home page after successful login
        else:
            # Display error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        role = request.POST.get('role', 'student')  # Get the role from POST data, default to 'student'
        if role == 'student':
            form = StudentCreationForm(request.POST)
        elif role == 'organizer':
            form = OrganiserCreationForm(request.POST)
        else:
            print("PARTICIPANT")
            form = UserCreationForm(request.POST)  # Default form

        if form.is_valid():
            print("VALID")
            print(form.cleaned_data['username'])
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password
            user.save()
            return redirect('login')  # Redirect to login page after successful account creation
        else:
            print("INVALID")
            print(form.errors)
    else:
        form = UserCreationForm()  # Default form for GET request

    return render(request, 'register.html', {'form': form})

def events_view(request):
    return render(request, 'events.html')