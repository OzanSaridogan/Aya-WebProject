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
    from .models import AyasBilgi
    ayas_bilgiler = AyasBilgi.objects.all().order_by('-tarih')
    return render(request, 'ayas.html', {'ayas_bilgiler': ayas_bilgiler})

def faydali_bilgiler_view(request):
    faydali_bilgiler = FaydaliBilgi.objects.all().order_by('-tarih')
    return render(request, 'faydali_bilgiler.html', {'faydali_bilgiler': faydali_bilgiler})

def galeri(request):
    return render(request, 'galeri.html')

def iletisim(request):
    return render(request, 'contact.html')



