from rest_framework import generics
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from django.http import HttpResponse

# Breed endpoints
class BreedListCreate(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

# Dog endpoints
class DogListCreate(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

#making this to make sure its working and somethings shows on website
def index(request):
    return HttpResponse("Welcome to the Dog App - Finally !!! Your Docker setup works!")
