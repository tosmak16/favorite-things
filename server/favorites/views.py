from rest_framework import generics, status, viewsets, mixins, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Count
import django_filters.rest_framework

from .serializers import (UserSerializer, FavoriteSerializer, LoginSerializer,
                          AuditlogSerializer, CategorySerializer, FavoriteDetailsSerializer)
from .models import Favorite, Category, Auditlog
from .helpers import (handle_decrement_rank, handle_increment_rank, handle_left_shift_rank,
                      handle_right_shift_rank, login_handler)


class UserCreateView(generics.CreateAPIView):

    """It handles User creation.
    """
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request,):
        user_data = request.data

        serialized_user_data = UserSerializer(data=user_data)
        if not serialized_user_data.is_valid():
            return Response(data=serialized_user_data.errors, status=status.HTTP_400_BAD_REQUEST)
        serialized_user_data.save()
        validated_data = serialized_user_data.validated_data
        username = validated_data.get("username")
        password = validated_data.get("password")

        return login_handler(username, password)


class LoginView(generics.CreateAPIView):

    """It has handles user authentication and returns token to authenticated user.
    """
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")

        return login_handler(username, password)


class FavoriteViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    """ It handles favorite operations like create and list of favorites. """
    serializer_class = FavoriteSerializer
    filter_backends = (filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend,)
    ordering_fields = ('ranking', 'category', 'created_date', 'modified_date')
    ordering = ('-modified_date',)
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Favorite.objects.filter(
            owner_id=self.request.user, is_deleted=False)
        return queryset

    def perform_create(self, serializer):

        category = serializer.validated_data.get('category')
        ranking = serializer.validated_data.get('ranking')

        # update favorite rank of the same category
        handle_increment_rank(ranking=ranking, category=category)

        serializer.save()


class FavoriteDetailsViewSet(
        mixins.RetrieveModelMixin, viewsets.GenericViewSet,
        mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    """ It handles favorite operations like update, retrieve and delete favorites. """
    serializer_class = FavoriteDetailsSerializer

    def get_queryset(self):
        queryset = Favorite.objects.filter(
            owner_id=self.request.user, is_deleted=False)
        return queryset

    def perform_update(self, serializer):

        instance = self.get_object()

        new_ranking = serializer.validated_data.get('ranking')
        new_category = serializer.validated_data.get('category')

        if (instance.ranking != new_ranking or instance.ranking == new_ranking) and instance.category != new_category:
            handle_increment_rank(ranking=new_ranking, category=new_category)
            handle_decrement_rank(ranking=instance.ranking, category=instance.category)

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
        instance.is_deleted = True
        instance.title = f'{instance.title}-{datetime.utcnow()}'
        instance.save()


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):

    """It handles category view operations like list and create categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(Count('favorites', distinct=True))
    pagination_class = None

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
        queryset = category.favorites.filter(
            owner_id=self.request.user, is_deleted=False)
        data = FavoriteSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class AuditLogView(generics.ListAPIView):

    """It handles get audit logs
    """

    serializer_class = AuditlogSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('created_date',)
    ordering = ('-created_date',)

    def get_queryset(self):
        queryset = Auditlog.objects.filter(owner_id=self.request.user)
        return queryset
