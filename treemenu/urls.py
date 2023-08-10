from django.urls import path
from . import views  
from lokomotiv import settings
from django.conf.urls.static import static


urlpatterns =[
path("",views.show_schemes,name="schemes"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
