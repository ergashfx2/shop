from django.contrib import admin

from notifications.models import Notifications


# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    model = Notifications
    list_display = ['title', 'body']


admin.site.register(Notifications, NotificationAdmin)