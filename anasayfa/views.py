from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Etkinlik
from .models import Duyuru, FaydaliBilgi


# Create your views here.

def anasayfa(request):
    return render(request, 'anasayfa2.html')

def etkinlik(request):
    etkinlikler = Etkinlik.objects.order_by('-tarih', '-saat')
    return render(request, 'etkinlik.html', {'etkinlikler': etkinlikler})

def duyurular(request):
    return render(request, 'duyurular.html')

def ayas(request):
    from .models import AyasBilgi
    ayas_bilgiler = AyasBilgi.objects.all().order_by('-tarih')
    return render(request, 'ayas.html', {'ayas_bilgiler': ayas_bilgiler})

def faydali_bilgiler(request):
    return render(request, 'faydali_bilgiler.html')

def galeri(request):
    return render(request, 'galeri.html')

def iletisim(request):
    return render(request, 'contact.html')

def contact(request):
    from django.core.mail import send_mail
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            subject = f'Yeni İletişim Mesajı: {name}'
            body = f'Gönderen: {name} <{email}>\n\nMesaj:\n{message}'
            send_mail(
                subject,
                body,
                'ozansari9@gmail.com',  # Change this to your sender email if needed
                ['ozansardogan379@gmail.com'],
                fail_silently=False,
            )
            success = True
    return render(request, 'contact.html', {'success': success})

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

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

def etkinlik_listesi(request):
    etkinlikler = Etkinlik.objects.all()
    return render(request, 'etkinlik.html', {'etkinlikler': etkinlikler})

def duyurular_view(request):
    duyurular = Duyuru.objects.all().order_by('-tarih')
    return render(request, 'duyurular.html', {'duyurular': duyurular})

def faydali_bilgiler_view(request):
    faydali_bilgiler = FaydaliBilgi.objects.all().order_by('-tarih')
    return render(request, 'faydali_bilgiler.html', {'faydali_bilgiler': faydali_bilgiler})



