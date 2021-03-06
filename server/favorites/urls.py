from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (UserCreateView, LoginView, FavoriteViewSet, AuditLogView,
                    CategoryViewSet, CategoryFavoriteView, FavoriteDetailsViewSet)

router = DefaultRouter()
router.register("favorites", FavoriteViewSet, base_name="favorites")
router.register("favorites", FavoriteDetailsViewSet, base_name="favorites")
router.register("categories", CategoryViewSet, base_name="categories")


urlpatterns = [
    path("users/", UserCreateView.as_view(), name="users"),
    path("login/", LoginView.as_view(), name="login"),
    path("categories/<int:category_id>/favorites/",
         CategoryFavoriteView.as_view(), name="category_favorite"),
    path("audit_logs/", AuditLogView.as_view(), name="audit_logs"),
]

urlpatterns += router.urls
