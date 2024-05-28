from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'date_of_birth', 'email', 'username', 'password', 'address', 'phone_number', 'account_number', 
            'account_balance', 'net_worth', 'investment_amount', 'investment_experience', 'risk_tolerance', 
            'identification_type', 'identification_number', 'identification_expiry_date', 'profile_picture', 
            'social_media_links', 'preferred_currency', 'preferred_language', 'created_at', 'groups', 
            'user_permissions'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance
