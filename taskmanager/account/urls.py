from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from account import views

urlpatterns = [
    path('profile/', views.ProfilView.as_view(), name='profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# The format_suffix_patterns function allows the API to respond to different formats like JSON or XML.