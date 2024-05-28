from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet
from .serializers import WalletSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
    operation_description="Get wallet details",
    responses={200: WalletSerializer}
)
def get_wallet(request):
    wallet = Wallet.objects.all()
    get_object_or_404(wallet, user=request.user)
    serializer = WalletSerializer(wallet)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(
    operation_description="Create a wallet",
    responses={201: WalletSerializer}
)
def create_wallet(request):
    serializer = WalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_wallet(request, pk):
    wallet = get_wallet(pk)
    serializer = WalletSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_wallet(request, pk):
    wallet = get_wallet(pk)
    wallet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)