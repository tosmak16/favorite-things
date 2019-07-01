from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Favorite, Category, Auditlog


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class FavoriteDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'
        extra_kwargs = {'owner': {'read_only': True},
                        'is_deleted': {'read_only': True}}


class AuditlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auditlog
        fields = '__all__'
