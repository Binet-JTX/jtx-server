from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from jtx_core.models.tag import TagViewSet, TagKeyViewSet
from jtx_events.models import EventViewSet

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'tagkeys', TagKeyViewSet)
router.register(r'events', EventViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
)
