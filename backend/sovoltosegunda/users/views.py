from users.serializers import AddUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class RegisterUserViewSet(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        add_user_serializer = AddUserSerializer(data=request.data)
        if add_user_serializer.is_valid(self):
           response = add_user_serializer.save()
           return response