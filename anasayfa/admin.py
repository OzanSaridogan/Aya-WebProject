from django.contrib import admin
from .models import (
	AyasBilgi,
	AyasTarihi,
	GezilecekYer,
	AyasKoyu,
	AyastanHaber,
	DigerBilgi,
)


@admin.register(AyasTarihi)
class AyasTarihiAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'kategori', 'sira', 'tarih')
	list_editable = ('sira',)
	list_filter = ('kategori',)
	search_fields = ('baslik', 'aciklama')
	ordering = ('kategori', 'sira', '-tarih')


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
	list_display = ('baslik', 'kategori', 'sira', 'tarih', 'yayinlanma_tarihi', 'aktif')
	list_editable = ('sira', 'aktif')
	list_filter = ('aktif', 'kategori')
	search_fields = ('baslik', 'aciklama')
	ordering = ('kategori', 'sira', '-tarih', '-yayinlanma_tarihi')


@admin.register(DigerBilgi)
class DigerBilgiAdmin(admin.ModelAdmin):
	list_display = ('baslik', 'kategori', 'sira', 'tarih')
	list_editable = ('sira',)
	list_filter = ('kategori',)
	search_fields = ('baslik', 'aciklama')
	ordering = ('kategori', 'sira', '-tarih')


admin.site.register(AyasBilgi)
