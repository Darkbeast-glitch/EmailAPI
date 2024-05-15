from django.urls import path
from .views import EmailCreateView, EmailListView

urlpatterns = [
    path('email', EmailCreateView.as_view(), name='create_email'),
    path('list-emails', EmailListView.as_view(), name='list_emails'),
]
