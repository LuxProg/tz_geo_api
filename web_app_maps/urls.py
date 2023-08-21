from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from maps.views import RoadGeometryAPIView, RoadGeometryDetailView, RoadAttrView, AzsFixedApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('maps/', include('maps.urls')),
    path('api1/', cache_page(60*5)(RoadGeometryAPIView.as_view())),
    path('api2/<int:road_code>/', cache_page(60*5)(RoadGeometryDetailView.as_view())),
    path('api3/<int:road_code>/', cache_page(60*5)(RoadAttrView.as_view())),
    path('api4/<int:road_code>/', AzsFixedApi.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
