from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'pub_date',)
    list_filter = ['pub_date']
admin.site.register(Poll, PollAdmin)