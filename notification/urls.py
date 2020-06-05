from django.urls import path
from notification import views

urlpatterns = [
    path('notification/<int:id>', views.notification, name='notification'),
]