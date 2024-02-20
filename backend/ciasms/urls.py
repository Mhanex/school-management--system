from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
# from  . import views
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # path('activate/', include('accounts.urls')),
    path('auth/jwt/create/',CustomTokenObtainPairView.as_view(),name='custom_jwt_create'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]