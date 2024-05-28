from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import HTTP_200_OK
from .models import Signal
from django.shortcuts import get_object_or_404
from .serializers import SignalSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='GET', responses={200: 'OK'})
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signal_list(request):
    signals = Signal.objects.all()
    serializer = SignalSerializer(signals, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@swagger_auto_schema(method='POST', request_body=SignalSerializer, responses={200: 'OK'})
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signal_create(request):
    serializer = SignalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='GET', responses={200: 'OK'})
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signal_detail(request, pk):
    signal = get_object_or_404(Signal, pk=pk)
    serializer = SignalSerializer(signal)
    return Response(serializer.data, status=HTTP_200_OK)

@swagger_auto_schema(method='PUT', request_body=SignalSerializer, responses={200: 'OK'})
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signal_update(request, pk):
    signal = get_object_or_404(Signal, pk=pk)
    serializer = SignalSerializer(signal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='DELETE', responses={204: 'NO CONTENT'})
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def signal_delete(request, pk):
    signal = get_object_or_404(Signal, pk=pk)
    signal.delete()
    return Response(status=HTTP_204_NO_CONTENT)
