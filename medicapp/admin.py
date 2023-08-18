from django.contrib import admin

# Register your models here.
from .models import Profile,Medical,Treatment


models_list = [Profile,Medical,Treatment]
admin.site.register(models_list)
