from django.urls import include, path
from django.conf.urls import url
from rest_framework.authtoken import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('^api/', include('favorites.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
