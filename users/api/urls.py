from django.urls import path
from users.api.views import CurrentUserAPIView, CurrentUserDetailAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("user/<int:pk>/", CurrentUserDetailAPIView.as_view(), name="user-detail")
]