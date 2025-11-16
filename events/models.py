from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    EVENT_TYPES = [
        ('workshop', 'Workshop'),
        ('meeting', 'Meeting'),
        ('competition', 'Competition'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    # Basic info
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image_url = models.URLField(blank=True, null=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    is_online = models.BooleanField(default=False)
    meeting_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    capacity = models.PositiveIntegerField(default=0)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)

    # Flexible fields as JSON/text
    organizers = models.TextField(blank=True, null=True)  # JSON string: ["Org1", "Org2"]
    tags = models.TextField(blank=True, null=True)        # JSON string: ["Tag1", "Tag2"]
    prerequisites = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    speakers = models.TextField(blank=True, null=True)    # JSON string of speaker objects
    schedule = models.TextField(blank=True, null=True)    # JSON string of schedule items
    resources = models.TextField(blank=True, null=True)   # JSON string of resources
    faqs = models.TextField(blank=True, null=True)        # JSON string of FAQs
    agenda = models.TextField(blank=True, null=True)      # JSON string of agenda items
    documents = models.TextField(blank=True, null=True)   # JSON string of document objects
    rules = models.TextField(blank=True, null=True)
    prizes = models.TextField(blank=True, null=True)
    judges = models.TextField(blank=True, null=True)
    sponsors = models.TextField(blank=True, null=True)
    social_links = models.TextField(blank=True, null=True)  # JSON string: {"facebook": "", "twitter": ""}
    registration_url = models.URLField(blank=True, null=True)
    recording_url = models.URLField(blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    difficulty = models.CharField(max_length=50, blank=True, null=True)
    registration_fee = models.FloatField(default=0)
    currency = models.CharField(max_length=10, default='USD')
    prize_pool = models.FloatField(blank=True, null=True)
    max_team_size = models.PositiveIntegerField(default=1)

    # Participants / registration
    participants = models.ManyToManyField(
        User,
        through='EventRegistration',
        related_name='events'
    )

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=255, blank=True, null=True)  # for team events
    team_members = models.TextField(blank=True, null=True)  # JSON string of team members if any
    registered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='pending')  # pending/paid

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

class EventRegistrationForNonMember(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="Contact Email")
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    phone = models.CharField(max_length=20, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=255, blank=True, null=True)  # for team events
    team_members = models.TextField(blank=True, null=True)  # JSON string of team members if any
    registered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='pending')  # pending/paid

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


    