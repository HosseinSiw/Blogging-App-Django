from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')), USER EXTENSION BUT NOT USED
    path("users/", include("users.urls")),
    path("", include('home.urls')),
    # path("algorithm", include('algorithms.urls'))
    # path('users', include('users.urls')),
]
