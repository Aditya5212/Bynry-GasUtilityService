from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Gas Leakage', 'Gas Leakage'),
        ('Billing Issue', 'Billing Issue'),
        ('New Connection', 'New Connection'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    SEVERITY_CHOICES = [
        (1, 'High Priority'),
        (2, 'Medium High Priority'),
        (3, 'Medium Priority'),
        (4, 'Medium Low Priority'),
        (5, 'Low Priority'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    severity = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES, default=3)  # Default to Medium Priority
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username} (Severity: {self.severity})"
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
