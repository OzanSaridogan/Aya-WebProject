from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('etkinlik/', views.etkinlik, name='etkinlik'),
    path('duyurular/', views.duyurular_view, name='duyurular'),
    path('ayas/', views.ayas, name='ayas'),
    path('faydali_bilgiler/', views.faydali_bilgiler_view, name='faydali_bilgiler'),
    path('galeri/', views.galeri, name='galeri'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('contact/', views.contact, name='contact'),  # Yeni iletişim sayfası için
    path('Login/', views.login_view, name='login'),  # Giriş sayfası
]

urlpatterns += staticfiles_urlpatterns()  # Static files için URL kalıplarını ekle
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media files için URL
