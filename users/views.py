from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User.objects
    serializer_class = UserSerializer