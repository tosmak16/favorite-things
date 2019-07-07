from django.db.models import F, Q
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status


from .models import Favorite


def handle_increment_rank(ranking, category):
    """It increases ranking when a new favorite is added"""

    Favorite.objects.filter(ranking__gte=ranking, category=category,
                            is_deleted=False).update(ranking=F('ranking')+1)


def handle_decrement_rank(ranking, category):
    """It decreases ranking when a favorite is removed"""

    Favorite.objects.filter(ranking__gt=ranking, category=category, is_deleted=False).update(
        ranking=F('ranking')-1)


def handle_right_shift_rank(new_ranking, current_ranking, category):
    """It right shift ranking when a favorite new ranking is lower than current ranking"""

    Favorite.objects.filter(Q(ranking__gte=new_ranking) & Q(ranking__lte=current_ranking),
                            category=category, is_deleted=False).update(ranking=F('ranking')+1)


def handle_left_shift_rank(new_ranking, current_ranking, category):
    """It left shift ranking when a favorite new ranking is greater than current ranking"""

    Favorite.objects.filter(Q(ranking__lte=new_ranking) & Q(ranking__gt=current_ranking),
                            category=category, is_deleted=False).update(ranking=F('ranking')-1)


def login_handler(username, password):
    user = authenticate(username=username, password=password)
    if user:
        return Response(
            {
                "token": user.auth_token.key, "userId": user.id, "message": "Login successful."},
            status=status.HTTP_200_OK)
    else:
        return Response({"error": "Wrong Credentials."}, status=status.HTTP_401_UNAUTHORIZED)
