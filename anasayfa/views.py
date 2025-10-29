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
    # Return Ayaş tarihi entries ordered by 'sira' then newest
    ayas_tarihi = AyasTarihi.objects.order_by('sira', '-tarih')

    return render(request, 'Ayas_tarihi.html', {
        'ayas_tarihi': ayas_tarihi,
    })

def gezilecek_yerler_view(request):
    gezilecek_yerler = GezilecekYer.objects.all().order_by('-tarih')
    return render(request, 'Gezilecek_yerler.html', {'gezilecek_yerler': gezilecek_yerler})

def ayas(request):
    # Import models here to avoid circular import issues at module import time
    ayas_bilgiler = AyasBilgi.objects.all().order_by('-tarih')
    context = {'ayas_bilgiler': ayas_bilgiler}

    return render(request, 'Guncel_Haberler.html', context)

def koyler(request):
    # Import models here to avoid circular import issues at module import time
    ayas_koyleri = AyasKoyu.objects.all().order_by('-tarih')
    context = {'ayas_koyleri': ayas_koyleri}

    return render(request, 'koyler.html', context)


def iletisim(request):
    return render(request, 'contact.html')


def guncel_haberler(request):
    """Render the 'Guncel_Haberler.html' template with active news items."""
    # Only show active news items, newest first
    ayastan_haberler = AyastanHaber.objects.filter(aktif=True).order_by('-tarih')
    return render(request, 'Guncel_Haberler.html', {'ayastan_haberler': ayastan_haberler})


def diger_view(request):
    """Render the 'Diger.html' template using DigerBilgi as the source."""
    faydali_bilgiler = DigerBilgi.objects.all().order_by('sira', '-tarih')
    return render(request, 'Diger.html', {'Diger': faydali_bilgiler})



