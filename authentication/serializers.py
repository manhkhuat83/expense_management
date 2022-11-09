from rest_framework import serializers
from authentication.models import User
from authentication.hashers import make_password, validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "is_active", "date_joined")
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"required": True},
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "date_joined": {"read_only": True},
        }


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "is_active", "date_joined")
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"required": True},
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "date_joined": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User(**validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = (
            "password",
            "current_password",
            "new_password",
        )
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "current_password": {"write_only": True, "required": True},
            "new_password": {"write_only": True, "required": True},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not "current_password" or not "new_password" in attrs:
            raise serializers.ValidationError(
                "Current password and new password is required"
            )
        if not validate_password(attrs["current_password"], self.instance.password):
            raise serializers.ValidationError("Current password is incorrect")
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data["new_password"])
        validated_data.pop("current_password")
        validated_data.pop("new_password")
        return instance
