from django.contrib import admin

# Register your models here.
from .models import Plant

admin.site.register(Plant)

#superuser = adminPlant psw = plant123 or 123plant needtocheck