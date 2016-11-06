from django.contrib import admin

# Register your models here.
from models import Person, SocialNetwork

admin.site.register(Person)
admin.site.register(SocialNetwork)
