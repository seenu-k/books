from django.urls import path, include
from rest_framework import routers
from .views import BookView, ExternalBookView

router = routers.DefaultRouter()
router.register(r'books', BookView, basename='Book')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('external-books/', ExternalBookView.as_view()),
]