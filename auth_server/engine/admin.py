from django.contrib import admin
from engine.models import User, AuthSecret
# Register your models here.

admin.site.register(User)
admin.site.register(AuthSecret)
