from django.apps import AppConfig


class FavoritesConfig(AppConfig):
    name = 'favorites'

    def ready(self):
        # everytime server restarts
        import favorites.signals
