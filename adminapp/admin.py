from django.contrib import admin
from adminapp.models import *
# Register your models here.
admin.site.register(Genres),
admin.site.register(Movies),
admin.site.register(Cast),
admin.site.register(Notification)