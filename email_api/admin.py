from django.contrib import admin
from .models import Email

# Register your models here.


class EmailAdmin(admin.ModelAdmin):
    # fields to display in list view
    list_display = ('id', 'subject', 'sent_at', 'status')
    search_fields = ['subject', 'content']  # fields to search
    list_filter = ('status', 'sent_at')  # fields to filter
    ordering = ['-sent_at']  # order by sent_at in descending order


admin.site.register(Email, EmailAdmin)
