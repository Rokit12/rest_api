from django.urls import path  
from app_api.views import Live_view


urlpatterns = [
	path('', Live_view.as_view()),
]