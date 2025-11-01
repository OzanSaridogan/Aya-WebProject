from django.db import models



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
    KATEGORI_SECENEKLERI = [
        ('genel', 'Genel Ayaş Tarihi'),
        ('sahsiyetler', 'İz Bırakan Şahsiyetler'),
        ('hikayeler', 'Hikayeler'),
        ('gelenekler', 'Gelenekler'),
    ]
    
    kategori = models.CharField(
        "Kategori", 
        max_length=20, 
        choices=KATEGORI_SECENEKLERI, 
        default='genel',
        help_text="İçeriğin ait olduğu kategori"
    )
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='ayas_tarihi/', blank=True, null=True)
    video = models.FileField("Video", upload_to='ayas_tarihi/videos/', blank=True, null=True)
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Ayaş Tarihi"
        verbose_name_plural = "Ayaş Tarihi"
        ordering = ['kategori', 'sira', '-tarih']

    def __str__(self):
        return f"{self.get_kategori_display()} - {self.baslik}"


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
    KATEGORI_SECENEKLERI = [
        ('genel', 'Genel'),
        ('mulakat', 'Ayaşlılar ile Mülakat'),
        ('gezelim', 'Gezelim Görelim Faaliyetleri'),
        ('siir', 'Şiirler'),
        ('yazi', 'Yazılar'),
        ('fotograf', 'Fotoğraflar'),
    ]
    
    kategori = models.CharField(
        "Kategori", 
        max_length=20, 
        choices=KATEGORI_SECENEKLERI, 
        default='genel',
        help_text="Haberin ait olduğu kategori"
    )
    baslik = models.CharField("Haber Başlığı", max_length=200)
    aciklama = models.TextField("Haber İçeriği")
    resim = models.ImageField("Haber Görseli", upload_to='ayas_haberler/', blank=True, null=True)
    video = models.FileField("Haber Videosu", upload_to='ayas_haberler/videos/', blank=True, null=True)
    tarih = models.DateField("Haber Tarihi")
    yayinlanma_tarihi = models.DateTimeField("Yayınlanma Tarihi", auto_now_add=True)
    aktif = models.BooleanField("Aktif", default=True, help_text="Haberi göster/gizle")
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Ayaş'tan Haber"
        verbose_name_plural = "Ayaş'tan Haberler"
        ordering = ['kategori', 'sira', '-tarih', '-yayinlanma_tarihi']

    def __str__(self):
        return f"{self.get_kategori_display()} - {self.baslik}"


class DigerBilgi(models.Model):
    KATEGORI_SECENEKLERI = [
        ('yemek', 'Ayaşa ait Yemek Tarifleri'),
        ('dergi', 'Ayaş Dergileri'),
    ]
    
    kategori = models.CharField(
        "Kategori", 
        max_length=20, 
        choices=KATEGORI_SECENEKLERI, 
        default='yemek',
        help_text="İçeriğin ait olduğu kategori"
    )
    baslik = models.CharField("Başlık", max_length=200)
    aciklama = models.TextField("Açıklama")
    resim = models.ImageField("Görsel", upload_to='diger_bilgiler/', blank=True, null=True)
    video = models.FileField("Video", upload_to='diger_bilgiler/videos/', blank=True, null=True)
    pdf_dosya = models.FileField("PDF Dosyası", upload_to='diger_bilgiler/pdf/', blank=True, null=True, 
                                 help_text="Dergi için PDF dosyası (sadece Ayaş Dergileri kategorisi için)")
    tarih = models.DateField("Tarih", auto_now_add=True)
    sira = models.IntegerField("Sıra", default=0, help_text="Gösterim sırası (küçükten büyüğe)")

    class Meta:
        verbose_name = "Diğer Bilgi"
        verbose_name_plural = "Diğer Bilgiler"
        ordering = ['kategori', 'sira', '-tarih']

    def __str__(self):
        return f"{self.get_kategori_display()} - {self.baslik}"




