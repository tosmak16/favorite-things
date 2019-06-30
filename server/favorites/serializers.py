from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='username'
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'email')
