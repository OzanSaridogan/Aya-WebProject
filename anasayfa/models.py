from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("Ad Soyad", max_length=100)
    email = models.EmailField("E-posta")
    message = models.TextField("Mesaj")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class AyasBilgi(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='ayas/', blank=True, null=True)
    video = models.FileField("Ayas Videosu", upload_to='ayas/videos/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Ayaş Bilgi"
        verbose_name_plural = "Ayaş Bilgileri"

    def __str__(self):
        return self.baslik


# New Models for Subheaders
class AyasTarihi(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='ayas_tarihi/', blank=True, null=True)
    video = models.FileField("Video", upload_to='ayas_tarihi/videos/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Ayaş Tarihi"
        verbose_name_plural = "Ayaş Tarihi"
        ordering = ['sira', '-tarih']

    def __str__(self):
        return self.baslik


class GezilecekYer(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='gezilecek_yerler/', blank=True, null=True)
    video = models.FileField("Video", upload_to='gezilecek_yerler/videos/', blank=True, null=True)
    konum = models.CharField("Konum", max_length=200, blank=True, null=True, help_text="Yer tarifi veya koordinat")
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Gezilecek Yer"
        verbose_name_plural = "Gezilecek Yerler"
        ordering = ['sira', '-tarih']

    def __str__(self):
        return self.baslik


class AyasKoyu(models.Model):
    baslik = models.CharField("Köy Adı", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='ayas_koyleri/', blank=True, null=True)
    video = models.FileField("Video", upload_to='ayas_koyleri/videos/', blank=True, null=True)
    nufus = models.CharField("Nüfus", max_length=100, blank=True, null=True)
    uzaklik = models.CharField("Merkeze Uzaklık", max_length=100, blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Ayaş Köyü"
        verbose_name_plural = "Ayaş Köyleri"
        ordering = ['sira', 'baslik']

    def __str__(self):
        return self.baslik


class AyastanHaber(models.Model):
    baslik = models.CharField("Haber Başlığı", max_length=200)
    aciklama = models.TextField("Haber İçeriği")
    resim = models.ImageField("Haber Görseli", upload_to='ayas_haberler/', blank=True, null=True)
    video = models.FileField("Haber Videosu", upload_to='ayas_haberler/videos/', blank=True, null=True)
    tarih = models.DateField("Haber Tarihi")
    yayinlanma_tarihi = models.DateTimeField("Yayınlanma Tarihi", auto_now_add=True)
    aktif = models.BooleanField("Aktif", default=True, help_text="Haberi göster/gizle")

    class Meta:
        verbose_name = "Ayaş'tan Haber"
        verbose_name_plural = "Ayaş'tan Haberler"
        ordering = ['-tarih', '-yayinlanma_tarihi']

    def __str__(self):
        return self.baslik


class DigerBilgi(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='diger_bilgiler/', blank=True, null=True)
    video = models.FileField("Video", upload_to='diger_bilgiler/videos/', blank=True, null=True)
    kategori = models.CharField("Kategori", max_length=100, blank=True, null=True, 
                                help_text="Örn: Kültür, Ekonomi, Ulaşım")
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Diğer Bilgi"
        verbose_name_plural = "Diğer Bilgiler"
        ordering = ['sira', '-tarih']

    def __str__(self):
        return self.baslik


# Existing Models
class Etkinlik(models.Model):
    baslik = models.CharField("Etkinlik Başlığı", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih")
    saat = models.TimeField("Saat")
    yer = models.CharField("Yer", max_length=200)
    resim = models.ImageField("Etkinlik Görseli", upload_to='etkinlikler/', blank=True, null=True)
    video = models.FileField("Etkinlik Videosu", upload_to='etkinlikler/videos/', blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Etkinlik"
        verbose_name_plural = "Etkinlikler"

    def __str__(self):
        return self.baslik


class Duyuru(models.Model):
    baslik = models.CharField("Duyuru Başlığı", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih", auto_now_add=True)
    resim = models.ImageField("Duyuru Görseli", upload_to='duyurular/', blank=True, null=True)
    video = models.FileField("Duyuru Videosu", upload_to='duyurular/videos/', blank=True, null=True)

    class Meta:
        verbose_name = "Duyuru"
        verbose_name_plural = "Duyurular"

    def __str__(self):
        return self.baslik


class FaydaliBilgi(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='faydali_bilgiler/', blank=True, null=True)
    video = models.FileField("Faydalı Bilgi Videosu", upload_to='faydali_bilgiler/videos/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    class Meta:
        verbose_name = "Faydalı Bilgi"
        verbose_name_plural = "Faydalı Bilgiler"

    def __str__(self):
        return self.baslik