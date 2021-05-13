from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views
from rest_framework.authtoken import views as authViews

urlpatterns = [
    path('register', views.RegisterAPI.as_view()),
    path('login', authViews.obtain_auth_token, name='api-token-auth'),
    path('logout', views.LogoutAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)