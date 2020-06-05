from django.urls import path
from twitteruser import views

urlpatterns = [
    path('twitter_user/<int:id>', views.twitter_user, name='twitter_user'),
]