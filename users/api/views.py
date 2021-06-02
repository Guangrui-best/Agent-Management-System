from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer
from users.models import CustomUser

from django.core.mail import send_mail
from django.conf import settings


class CurrentUserAPIView(generics.ListCreateAPIView):
    # print(CustomUser.email)
    # print(os.environ.get('EMAIL_HOST_USER', ''))
    queryset = CustomUser.objects.all().order_by("-id")
    serializer_class = UserDisplaySerializer
    # permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    def perform_create(self, serializer):
        created_object = serializer.save()
        send_mail("Successful Registration as Agent at Antai Global Inc.",
                  "Dear " + str(created_object.username) + 
                  ",\n\nThank you for your registration. Your member id is " + 
                  str(created_object.id) + 
                  ". Hope you enjoy our web services!\n\nBest,\nAntai Global Inc.",
                  settings.EMAIL_HOST_USER,
                  [created_object.email],
                  fail_silently=False)
                  

class CurrentUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDisplaySerializer
    # permission_classes = [IsAdminUserOrReadOnly]

# class CurrentUserAPIView(APIView):

#     def get(self, request):
#         serializer = UserDisplaySerializer(request.user)
#         return Response(serializer.data)
