from django.db import models


class Notice(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateField()
    last_updated = models.DateField(auto_now=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    views = models.PositiveIntegerField(default=0)
    attachments = models.TextField(
        blank=True,
        null=True,
        help_text='Store attachments as JSON string: [{"name": "file.pdf", "url": "https://..."}]'
    )

    def __str__(self):
        return self.title
