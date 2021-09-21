from django.contrib import admin
from .models import Corporate, Environment, Governance, Social, News
# Register your models here.

admin.site.register([Corporate, Environment, Governance, Social, News])
