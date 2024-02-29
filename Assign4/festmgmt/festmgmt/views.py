from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, StudentCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('events.html')  # Redirect to home page after successful login
        else:
            # Display error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(login_view)  # Redirect to login page after successful account creation
    else:
        form = StudentCreationForm()
    return render(request, 'register.html', {'form': form})
