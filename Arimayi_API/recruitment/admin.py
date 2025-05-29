# In admin.py
from django.contrib import admin
from .models import User, Candidat, Recruteur, Candidature

admin.site.register(User)
admin.site.register(Candidat)
admin.site.register(Recruteur)
admin.site.register(Candidature)
