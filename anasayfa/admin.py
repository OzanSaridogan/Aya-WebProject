from django.contrib import admin
from .models import (
	Etkinlik,
	Duyuru,
	FaydaliBilgi,
	AyasBilgi,
	ContactMessage,
	AyasTarihi,
	GezilecekYer,
	AyasKoyu,
	AyastanHaber,
	DigerBilgi,
)


@admin.register(AyasTarihi)
class AyasTarihiAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'sira', 'tarih')
	list_editable = ('sira',)
	search_fields = ('baslik', 'aciklama')
	ordering = ('sira', '-tarih')


@admin.register(GezilecekYer)
class GezilecekYerAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'konum', 'sira', 'tarih')
	list_filter = ('konum',)
	search_fields = ('baslik', 'aciklama', 'konum')
	ordering = ('sira', '-tarih')


@admin.register(AyasKoyu)
class AyasKoyuAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'nufus', 'uzaklik', 'sira')
	search_fields = ('baslik', 'aciklama')
	ordering = ('sira', 'baslik')


@admin.register(AyastanHaber)
class AyastanHaberAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'tarih', 'yayinlanma_tarihi', 'aktif')
	list_filter = ('aktif',)
	search_fields = ('baslik', 'aciklama')
	ordering = ('-tarih', '-yayinlanma_tarihi')


@admin.register(DigerBilgi)
class DigerBilgiAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'kategori', 'sira', 'tarih')
	list_filter = ('kategori',)
	search_fields = ('baslik', 'aciklama', 'kategori')
	ordering = ('sira', '-tarih')


admin.site.register(Etkinlik)
admin.site.register(Duyuru)
admin.site.register(FaydaliBilgi)
admin.site.register(AyasBilgi)
admin.site.register(ContactMessage)
