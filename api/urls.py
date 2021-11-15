# from django.urls import path
# from .views import BookView, ExternalBookView

# urlpatterns = [
#     path('v1/books/', BookView.as_view({'get': 'list'})),
#     path('external-books/', ExternalBookView.as_view()),
# ]

from django.urls import path, include
from rest_framework import routers
from .views import BookView, ExternalBookView

router = routers.DefaultRouter()
router.register(r'books', BookView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('external-books/', ExternalBookView.as_view()),
]