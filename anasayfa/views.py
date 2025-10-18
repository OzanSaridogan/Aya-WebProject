from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import Etkinlik, Duyuru, FaydaliBilgi, ContactMessage
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
def message_list(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('/')
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'message_list.html', {'messages': messages})

def contact(request):
    return render(request, 'contact.html')

def anasayfa(request):
    return render(request, 'anasayfa2.html')

def etkinlik(request):
    etkinlikler = Etkinlik.objects.order_by('-tarih', '-saat')
    return render(request, 'etkinlik.html', {'etkinlikler': etkinlikler})

def duyurular_view(request):
    duyurular = Duyuru.objects.all().order_by('-tarih')
    return render(request, 'duyurular.html', {'duyurular': duyurular})

def ayas(request):
    # Import models here to avoid circular import issues at module import time
    from .models import (
        AyasBilgi,
        AyasTarihi,
        GezilecekYer,
        AyasKoyu,
        AyastanHaber,
        DigerBilgi,
    )

    context = {}

    # Legacy single-list (if AyasBilgi is still used elsewhere)
    try:
        context['ayas_bilgiler'] = AyasBilgi.objects.all().order_by('-tarih')
    except Exception:
        context['ayas_bilgiler'] = []

    # New category-wise lists (added via admin)
    context['ayas_tarihi'] = AyasTarihi.objects.all().order_by('sira', '-tarih')
    context['gezilecek_yerler'] = GezilecekYer.objects.all().order_by('sira', '-tarih')
    context['ayas_koyleri'] = AyasKoyu.objects.all().order_by('sira', 'baslik')
    context['ayas_haberleri'] = AyastanHaber.objects.filter(aktif=True).order_by('-tarih', '-yayinlanma_tarihi')
    context['diger_bilgiler'] = DigerBilgi.objects.all().order_by('sira', '-tarih')

    return render(request, 'ayas.html', context)

def faydali_bilgiler_view(request):
    faydali_bilgiler = FaydaliBilgi.objects.all().order_by('-tarih')
    return render(request, 'faydali_bilgiler.html', {'faydali_bilgiler': faydali_bilgiler})

def galeri(request):
    return render(request, 'galeri.html')

def iletisim(request):
    return render(request, 'contact.html')



