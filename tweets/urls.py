from django.urls import path
from .views import ListCreateTweetsView


urlpatterns = [
    path('', ListCreateTweetsView.as_view()),
]
