from rest_framework.generics import ListCreateAPIView
from .models import Tweet
from .serializers import TweetSerializer

# Create your views here.
class ListCreateTweetsView(ListCreateAPIView):
    queryset = Tweet
    serializer_class = TweetSerializer