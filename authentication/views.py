from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse
from authentication.models import User
from authentication.serializers import (
    UserSerializer,
    UserRegisterSerializer,
    ChangePasswordSerializer,
)


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            user = User.objects.get(email=request.data.get("email"))
            err = {"err": "User with this email already exists"}
            return JsonResponse(err, status=303)
        except:
            pass
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class SelfInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data, status=200)

    def put(self, request):
        user = self.request.user
        serializer = ChangePasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            msg = {"msg": "Password changed successfully"}
            return JsonResponse(msg, status=200)
        return JsonResponse(serializer.errors, status=400)
