from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from jtx_core.models.user import UserViewSet
from jtx_core.models.tag import TagViewSet, TagKeyViewSet
from jtx_video.views import VideoViewSet, ProjectionViewSet
from jtx_events.models import EventViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tagkeys', TagKeyViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'projections', ProjectionViewSet)
router.register(r'events', EventViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^', include(router.urls))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()