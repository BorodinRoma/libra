from django.urls import include, re_path
from rest_framework.routers import BaseRouter


def create_urlpatterns(routers: (str, BaseRouter)) -> []:
    urlpatterns = []
    for name, router in routers:
        urlpatterns.append(
            re_path(name, include(router.urls))
        )
    return urlpatterns