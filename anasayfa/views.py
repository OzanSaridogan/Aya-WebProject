from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import (
    AyasBilgi,
    AyasKoyu,
    GezilecekYer,
    AyasTarihi,
    AyastanHaber,
    DigerBilgi,
)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpResponse
import hashlib

# Create your views here.


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            error = 'Kullanıcı adı veya şifre yanlış.'
    return render(request, 'login.html', {'error': error})




@login_required


def contact(request):
    return render(request, 'contact.html')

def anasayfa(request):
    return render(request, 'anasayfa2.html')

def ayas_tarihi(request):
    # Return Ayaş tarihi entries grouped by category
    ayas_tarihi_all = AyasTarihi.objects.all().order_by('kategori', 'sira', '-tarih')
    
    # Group by category
    kategoriler = {
        'genel': [],
        'sahsiyetler': [],
        'hikayeler': [],
        'gelenekler': []
    }
    
    for item in ayas_tarihi_all:
        kategoriler[item.kategori].append(item)
    
    return render(request, 'Ayas_tarihi.html', {
        'kategoriler': kategoriler,
    })

def gezilecek_yerler_view(request):
    gezilecek_yerler = GezilecekYer.objects.all().order_by('-tarih')
    return render(request, 'Gezilecek_yerler.html', {'gezilecek_yerler': gezilecek_yerler})

def ayas(request):
    # Ayaş Bilgileri view - should use its own template, not Guncel_Haberler
    # This function appears to be unused or misconfigured
    # If you need Ayaş Bilgileri, create a separate template for it
    ayas_bilgiler = AyasBilgi.objects.all().order_by('-tarih')
    context = {'ayas_bilgiler': ayas_bilgiler}
    
    # TODO: Create a proper template for AyasBilgi or remove this view if not needed
    return render(request, 'ayas_bilgileri.html', context)

def koyler(request):
    # Import models here to avoid circular import issues at module import time
    ayas_koyleri = AyasKoyu.objects.all().order_by('-tarih')
    context = {'ayas_koyleri': ayas_koyleri}

    return render(request, 'koyler.html', context)


def iletisim(request):
    return render(request, 'contact.html')


def guncel_haberler(request):
    """Render the 'Guncel_Haberler.html' template with active news items grouped by category."""
    # Only show active news items
    haberler_all = AyastanHaber.objects.filter(aktif=True).order_by('kategori', 'sira', '-tarih')
    
    # Group by category
    kategoriler = {
        'genel': [],
        'mulakat': [],
        'gezelim': [],
        'siir': [],
        'yazi': [],
        'fotograf': []
    }
    
    for item in haberler_all:
        kategoriler[item.kategori].append(item)
    
    return render(request, 'Guncel_Haberler.html', {'kategoriler': kategoriler})


def diger_view(request):
    """Render the 'Diger.html' template using DigerBilgi as the source."""
    diger_bilgiler_all = DigerBilgi.objects.all().order_by('kategori', 'sira', '-tarih')
    
    # Group by category
    kategoriler = {
        'yemek': [],
        'dergi': []
    }
    
    for item in diger_bilgiler_all:
        kategoriler[item.kategori].append(item)
    
    return render(request, 'Diger.html', {'kategoriler': kategoriler})



