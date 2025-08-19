from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .serializers import RegistrationSerializer, ProfileSerializer, UpdatePasswordSerializer
from .permissions import IsNotDeleted


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsNotDeleted]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save(last_profile_update=timezone.now())


class UpdatePasswordView(generics.UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated, IsNotDeleted]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        
        send_mail(
            subject="Password Changed",
            message="Your password was changed successfully.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)


class SoftDeleteProfileView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsNotDeleted]

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.soft_delete()

    def delete(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response({"detail": "Account soft-deleted."}, status=status.HTTP_200_OK)


class AdminUserListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        status_filter = self.request.query_params.get('status', 'active')
        if status_filter == 'deleted':
            return User.objects.filter(is_deleted=True)
        elif status_filter == 'all':
            return User.objects.all()
        return User.objects.filter(is_deleted=False)


class RestoreUserView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return User.objects.filter(is_deleted=True)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.restore()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
