from django.urls import include, path
from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url('^api/', include('favorites.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/docs/', include_docs_urls(title='Favorite things API')),
]
