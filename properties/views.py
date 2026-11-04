from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Property


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


# Property details page
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    return render(request, 'property_detail.html', {
        'property': property
    })


# Buy property enquiry page
def buy_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        messages.success(
            request,
            'Your purchase enquiry has been submitted!'
        )
        return redirect('property_detail', property_id=property.id)

    return render(request, 'buy_property.html', {
        'property': property
    })


# Contact owner page
def contact_owner(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        messages.success(
            request,
            'Your contact enquiry has been submitted!'
        )
        return redirect('property_detail', property_id=property.id)

    return render(request, 'contact_owner.html', {
        'property': property
    })
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
# User Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# User Dashboard
@login_required(login_url='user_login')
def dashboard(request):
    return render(request, 'dashboard.html')


# User Logout
@login_required(login_url='user_login')
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_login')

    return redirect('dashboard')