
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/',views.contact, name = 'contact'),
     path('', views.home, name = 'home'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
