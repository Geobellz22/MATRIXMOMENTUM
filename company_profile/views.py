from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CompanyProfile
from .serializers import CompanyProfileSerializer

class CompanyProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]
    
class CompanyProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]
    
    