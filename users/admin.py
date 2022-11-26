from django.contrib import admin
from .models import CustomUser, Jwt

admin.site.register((CustomUser, ))
