from django.contrib import admin
from .models import Email

# Register your models here.


class EmailAdmin(admin.ModelAdmin):
    # fields to display in list view
    list_display = ('id', 'email')
    search_fields = ['email',]  # fields to search
    list_filter = ('id', 'email')  # fields to filter
    ordering = ['id']  # order by sent_at in descending order


admin.site.register(Email, EmailAdmin)
