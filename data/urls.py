from django.urls import path
from . import views  
from lokomotiv import settings
from django.conf.urls.static import static


urlpatterns =[
path("",views.import_excel,name="Import_Excel_pandas"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
