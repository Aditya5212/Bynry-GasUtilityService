from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest



@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_requests')  # Redirect to a tracking page
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

@login_required
def track_requests(request):
    # Fetch all service requests submitted by the logged-in customer
    service_requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')

    return render(request, 'customer_service/track_requests.html', {'service_requests': service_requests})

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')
	

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('track_requests')  # Redirect to the track requests page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'navbar/home.html')


from .forms import SignUpForm
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'customer_service/register.html', {'form':form})

	return render(request, 'customer_service/register.html', {'form':form})

from django.shortcuts import get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def modify_request(request, request_id):
    # Fetch the service request using the request_id
    service_request = get_object_or_404(ServiceRequest, id=request_id, customer=request.user)
    
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been updated successfully!")
            return redirect('track_requests')  # Redirect to the tracking page after successful update
    else:
        form = ServiceRequestForm(instance=service_request)
    
    return render(request, 'customer_service/modify_request.html', {'form': form, 'service_request': service_request})


def delete_request(request, request_id):
	if request.user.is_authenticated:
		delete_it = ServiceRequest.objects.get(id=request_id)
		delete_it.delete()
		messages.success(request, "Request Deleted Successfully...")
		return redirect('track_requests')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')