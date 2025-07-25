from django.contrib import admin

from .models import Etkinlik, Duyuru, FaydaliBilgi, AyasBilgi, ContactMessage

admin.site.register(Etkinlik)
admin.site.register(Duyuru)
admin.site.register(FaydaliBilgi)
admin.site.register(AyasBilgi)
admin.site.register(ContactMessage)
