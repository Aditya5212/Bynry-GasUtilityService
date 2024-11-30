from django.contrib import admin

# Register your models here.
# admin.py
from .models import ServiceRequest, CustomerProfile  # Import your models

# Register your models here
admin.site.register(ServiceRequest)  # Register ServiceRequest model
admin.site.register(CustomerProfile)  # Register CustomerProfile model
