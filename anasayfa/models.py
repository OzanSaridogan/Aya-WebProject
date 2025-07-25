
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
    tarih = models.DateField("Tarih", auto_now_add=True)

    def __str__(self):
        return self.baslik


class Etkinlik(models.Model):
    baslik = models.CharField("Etkinlik Başlığı", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih")
    saat = models.TimeField("Saat")
    yer = models.CharField("Yer", max_length=200)
    resim = models.ImageField("Etkinlik Görseli", upload_to='etkinlikler/', blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

class Duyuru(models.Model):
    baslik = models.CharField("Duyuru Başlığı", max_length=200)
    aciklama = models.TextField("Açıklama")
    tarih = models.DateField("Tarih", auto_now_add=True)
    resim = models.ImageField("Duyuru Görseli", upload_to='duyurular/', blank=True, null=True)

    def __str__(self):
        return self.baslik

class FaydaliBilgi(models.Model):
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='faydali_bilgiler/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)

    def __str__(self):
        return self.baslik
