from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from device import views

urlpatterns = [
 path('device/', views.DeviceList.as_view()),
 path('device/<str:pk>/', views.DeviceDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
