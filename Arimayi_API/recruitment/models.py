from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('candidat', 'Candidat'),
        ('recruteur', 'Recruteur'),
    )
    full_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

class Candidat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidat_profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    cv_url = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Recruteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recruteur_profile')
    company_name = models.CharField(max_length=255)
    company_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name

class Candidature(models.Model):
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidat.user.username} → {self.recruteur.company_name}"
