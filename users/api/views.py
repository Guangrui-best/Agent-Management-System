from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer
from users.models import CustomUser

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework import status
from users.forms import CustomUserForm
import os


@api_view(["GET", "POST"])
def user_list_create_api_view(request):
    
    if request.method == "GET":
        users = CustomUser.object.all()
        serializer = UserDisplaySerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserDisplaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(subject="Successful Registration as Agent at Antai Global Inc.",
                      from_email=os.environ.get('EMAIL_HOST_USER', ''),
                      recipient_list=[request.email],
                      fail_silently=True,
                      html_message="Dear " + str(request.username) + 
                      ",<br><br>Thank you for your registration. Your member id is " + 
                      str(request.id) + 
                      ". Hope you enjoy our web services!<br><br>Best,<br>Antai Global Inc.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CurrentUserAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by("-id")
    serializer_class = UserDisplaySerializer
    # permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]

class CurrentUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDisplaySerializer
    # permission_classes = [IsAdminUserOrReadOnly]

# class CurrentUserAPIView(APIView):

#     def get(self, request):
#         serializer = UserDisplaySerializer(request.user)
#         return Response(serializer.data)
