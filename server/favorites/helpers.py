from django.db.models import F, Q

from .models import Favorite


def handle_increment_rank(ranking, category):
    Favorite.objects.filter(ranking__gte=ranking, category=category).update(
        ranking=F('ranking')+1)


def handle_decrement_rank(ranking, category):
    Favorite.objects.filter(ranking__gt=ranking, category=category).update(
        ranking=F('ranking')-1)


def handle_right_shift_rank(new_ranking, current_ranking, category):
    Favorite.objects.filter(Q(ranking__gte=new_ranking) & Q(ranking__lte=current_ranking),
                            category=category).update(ranking=F('ranking')+1)


def handle_left_shift_rank(new_ranking, current_ranking, category):
    Favorite.objects.filter(Q(ranking__lte=new_ranking) & Q(ranking__gt=current_ranking),
                            category=category).update(ranking=F('ranking')-1)
