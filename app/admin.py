from django.contrib import admin

from .models import *

admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(House)
admin.site.register(Room)
admin.site.register(HouseMembership)
admin.site.register(Expense)
admin.site.register(CalendarEntry)
