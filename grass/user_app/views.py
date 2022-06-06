from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

# Create your views here.
@csrf_exempt
class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
