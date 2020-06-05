from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/<int:id>', views.tweet, name='tweet'),
]