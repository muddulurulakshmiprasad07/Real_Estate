from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Property

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Property
from .forms import RegisterForm


# HOME PAGE - LOGIN REQUIRED
@login_required(login_url='/login/')
def home(request):
    properties = Property.objects.all().order_by('-created_at')

    search = request.GET.get('search')

    if search:
        properties = properties.filter(
            location__icontains=search
        )

    return render(request, 'index.html', {
        'properties': properties
    })


# PROPERTY DETAILS
@login_required(login_url='/login/')
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'property_detail.html', {
        'property': property
    })


# REGISTER
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# LOGIN
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# DASHBOARD
@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')


# LOGOUT
@login_required(login_url='/login/')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_login')

    return redirect('dashboard')


# Property details - login required
@login_required(login_url='user_login')
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    return render(request, 'property_detail.html', {
        'property': property
    })


# Buy property - login required
@login_required(login_url='user_login')
def buy_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        messages.success(request, 'Purchase enquiry submitted!')
        return redirect('property_detail', property_id=property.id)

    return render(request, 'buy_property.html', {
        'property': property
    })


# Contact owner - login required
@login_required(login_url='user_login')
def contact_owner(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        messages.success(request, 'Contact enquiry submitted!')
        return redirect('property_detail', property_id=property.id)

    return render(request, 'contact_owner.html', {
        'property': property
    })
    # USER REGISTRATION
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# USER LOGIN
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# USER DASHBOARD
@login_required(login_url='user_login')
def dashboard(request):
    return render(request, 'dashboard.html')


# USER LOGOUT
@login_required(login_url='user_login')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_login')

    return redirect('dashboard')
