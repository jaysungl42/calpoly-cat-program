from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from backend.serializers import *
from directory.models import Cat 
from directory.models import Document 
from directory.models import Event

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer 

    def get_queryset(self):
        queryset = Document.objects.all()
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset
        
class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer 

    def get_queryset(self):
        queryset = Photo.objects.all()
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset
        
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer 

    def get_queryset(self):
        queryset = Event.objects.all()
        cat_id = self.request.query_params.get('cat_id', None)
        if cat_id is not None:
            queryset = queryset.filter(cat_id=cat_id)
        return queryset
