from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
import uuid

class Invoice(models.Model):
    INVOICE_TYPE = [
        ('event', 'Event Payment'),
        ('membership', 'Monthly Fee'),
        ('registration_fee', 'Registration Fee'), 
        ('recruitment_fee', 'Recruitment Fee'), 
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
        ('overdue', 'Overdue'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    invoice_type = models.CharField(max_length=20, choices=INVOICE_TYPE, default='other')
    # related_event = models.ForeignKey('Event', on_delete=models.SET_NULL, blank=True, null=True, related_name='invoices')
    paying_id = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    currency = models.CharField(max_length=10, default='BST')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.user.username}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('card', 'Credit/Debit Card'),
        ('bkash', 'bKash'),
        ('paypal', 'PayPal'),
        ('bank', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='payment')
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment for {self.invoice.invoice_number} - {self.status}"
