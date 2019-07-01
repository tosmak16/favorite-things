from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import F

from .serializers import (UserSerializer, FavoriteSerializer,
                          CategorySerializer, FavoriteDetailsSerializer)
from .models import Favorite, Category
from .helpers import (handle_decrement_rank, handle_increment_rank,
                      handle_left_shift_rank, handle_right_shift_rank)


class UserCreateView(generics.CreateAPIView):

    """It handles User creation.
    """
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()


class LoginView(APIView):

    """It has handles user authentication and returns token to authenticated user.
    """
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key, "message": "Login successful"})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class FavoriteViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    """ It handles favorite operations like create and list of favorites. """
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.filter(owner_id=self.request.user)
        return queryset

    def perform_create(self, serializer):

        # update favorite rank of the same category
        handle_increment_rank(ranking=serializer.validated_data.get(
            'ranking'), category=serializer.validated_data.get('category'))

        serializer.save()


class FavoriteDetailsViewSet(
        mixins.RetrieveModelMixin, viewsets.GenericViewSet,
        mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    """ It handles favorite operations like update, retrieve and delete favorites. """
    serializer_class = FavoriteDetailsSerializer

    def get_queryset(self):
        queryset = Favorite.objects.filter(owner_id=self.request.user)
        return queryset

    def perform_update(self, serializer):

        instance = self.get_object()

        new_ranking = serializer.validated_data.get('ranking')
        new_category = serializer.validated_data.get('category')

        if (instance.ranking != new_ranking or instance.ranking == new_ranking) and instance.category != new_category:
            handle_increment_rank(ranking=new_ranking, category=new_category)
            handle_decrement_rank(ranking=instance.ranking,
                                  category=instance.category)

        elif new_ranking > instance.ranking and instance.category == new_category:
            handle_left_shift_rank(new_ranking, instance.ranking, new_category)

        elif new_ranking < instance.ranking and instance.category == new_category:
            handle_right_shift_rank(
                new_ranking, instance.ranking, new_category)
        serializer.save()

    def perform_destroy(self, instance):

        # update favorite rank of the same category
        handle_decrement_rank(ranking=instance.ranking,
                              category=instance.category)
        instance.delete()


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):

    """It handles category view operations like list and create categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request):

        category_data = dict(name=request.data.get('name', '').lower())
        serializer = CategorySerializer(data=category_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryFavoriteView(generics.ListAPIView):

    """This view returns favorites associated with a category.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        queryset = category.favorites.filter(owner_id=self.request.user)
        data = FavoriteSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
