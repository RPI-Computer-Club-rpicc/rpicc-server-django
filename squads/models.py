from django.db import models
from django.contrib.auth.models import User


class Squad(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class SquadMembership(models.Model):
    ROLE_CHOICES = [
        ("Leader", "Squad Leader"),
        ("Executive", "Extra Executive Member"),
        ("Member", "Squad Member"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    class Meta:
        unique_together = ('user', 'squad')

    def __str__(self):
        return f"{self.user.username} - {self.squad.name} ({self.role})"

