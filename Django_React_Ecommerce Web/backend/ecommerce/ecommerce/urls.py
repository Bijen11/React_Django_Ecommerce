
from django.contrib import admin
from django.urls import path , include , re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'myApp'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    path('api/' , include('Product.api.urls')),
    path('account/' , include('accounts.urls')),
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html')) ]


