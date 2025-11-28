from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('Ayas_tarihi/', views.ayas_tarihi, name='Ayas_tarihi'),
    path('Gezilecek_yerler/', views.gezilecek_yerler_view, name='Gezilecek_yerler'),
    path('koyler/', views.koyler, name='koyler'),
    path('Diger/', views.diger_view, name='Diger'),
    path('Guncel_Haberler/', views.guncel_haberler, name='guncel_haberler'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('contact/', views.contact, name='contact'),
    path('Login/', views.login_view, name='login'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
