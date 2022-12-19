from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
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
            err = {"err": "See other"}
            return JsonResponse(err, status=303)
        except:
            pass
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelfInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = self.request.user
        serializer = ChangePasswordSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            msg = {"msg": "Changed"}
            return JsonResponse(msg, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
