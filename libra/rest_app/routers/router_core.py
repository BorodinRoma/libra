from rest_framework import routers

from rest_app.viewsets.core import BookViewset

router = routers.DefaultRouter()

router.register('book', BookViewset, 'book')