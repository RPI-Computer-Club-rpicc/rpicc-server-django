from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import URLValidator



class UserDetails(models.Model):

    PRIMARY_ROLE_CHOICES = [
        ('Member', 'Member'),

        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('General Secretary', 'General Secretary'),
        ('Joint General Secretary', 'Joint General Secretary'),

        ('Organisation Secretary', 'Organisation Secretary'),
        ('Associate Organisation Secretary', 'Associate Organisation Secretary'),

        ('Treasurer', 'Treasurer'),
        ('Associate Treasurer', 'Associate Treasurer'),

        ('Events & Management Secretary', 'Events & Management Secretary'),
        ('Associate Events & Management Secretary', 'Associate Events & Management Secretary'),

        ('Publicity Secretary', 'Publicity Secretary'),
        ('Associate Publicity Secretary', 'Associate Publicity Secretary'),

        ('Publications Secretary', 'Publications Secretary'),
        ('Associate Publications Secretary', 'Associate Publications Secretary'),

        ('Official Secretary', 'Official Secretary'),
        ('Associate Official Secretary', 'Associate Official Secretary'),

        ('Executive Member', 'Executive Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='details')
    primary_role = models.CharField(max_length=100, choices=PRIMARY_ROLE_CHOICES, default='Member')

    department = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    session = models.CharField(max_length=20)
    designation = models.CharField(max_length=255)
    quote = models.CharField(max_length=200)
    bio = models.TextField()

    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    webmail = models.CharField(max_length=255, blank=True, null=True)

    facebook = models.URLField(validators=[URLValidator()], blank=True, null=True)
    instagram = models.URLField(validators=[URLValidator()], blank=True, null=True)
    linkedin = models.URLField(validators=[URLValidator()], blank=True, null=True)
    github = models.URLField(validators=[URLValidator()], blank=True, null=True)
    twitter = models.URLField(validators=[URLValidator()], blank=True, null=True)
    website = models.URLField(validators=[URLValidator()], blank=True, null=True)

    image = models.URLField(validators=[URLValidator()], blank=True, null=True)
    join_date = models.DateField()
    term = models.CharField(max_length=20)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-join_date']
        verbose_name = 'User Details'
        verbose_name_plural = 'User Details'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.primary_role}"

    # ─────────────────────────────────────
    #  RBAC — ASSIGN GROUPS AUTOMATICALLY
    # ─────────────────────────────────────
    def assign_groups(self):
        # Ensure a default Member group exists
        member_group, _ = Group.objects.get_or_create(name="Member")

        # Remove old groups
        self.user.groups.clear()

        # Add Member group always
        self.user.groups.add(member_group)

        # Add selected role (e.g., President, Treasurer)
        # role_group, _ = Group.objects.get_or_create(name=self.primary_role)
        # self.user.groups.add(role_group)

    # ─────────────────────────────────────
    #  SAVE OVERRIDE
    # ─────────────────────────────────────
    def save(self, *args, **kwargs):
        # Sync email inside main User model
        if not self.user.email:
            self.user.email = self.email
            self.user.save()

        super().save(*args, **kwargs)

        # Assign RBAC Groups
        self.assign_groups()