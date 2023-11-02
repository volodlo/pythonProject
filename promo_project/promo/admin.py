from django.contrib import admin
from .models import Person, Campaign, House


admin.site.register(Person)
admin.site.register(Campaign)
admin.site.register(House)