from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets, permissions
from .models import Users
from .serializers import UsersSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser



class UsersView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'retrieve' or self.action == 'list' or self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]
