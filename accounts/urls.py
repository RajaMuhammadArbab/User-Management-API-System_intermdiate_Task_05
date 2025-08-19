from django.urls import path
from .views import (
    RegisterView, ProfileView, UpdatePasswordView, SoftDeleteProfileView,
    AdminUserListView, RestoreUserView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/password/', UpdatePasswordView.as_view(), name='update-password'),
    path('profile/delete/', SoftDeleteProfileView.as_view(), name='soft-delete'),
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('admin/users/restore/<int:pk>/', RestoreUserView.as_view(), name='restore-user'),
]
