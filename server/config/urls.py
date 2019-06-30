from django.urls import include
from django.conf.urls import url


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('^api/', include('favorites.urls')),
]
