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

""""
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

"""
def login_view(request):
    """
    ❌ TEHLİKELİ: Raw SQL sorgusu ile string concatenation
    
    Saldırı:
    username: admin' OR '1'='1' --
    password: herhangi
    
    Bu kod SQL Injection'a tamamen açık!
    """
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Şifreyi hash'le (yine de güvensiz!)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        # ❌ GÜVENSIZ: String concatenation ile SQL sorgusu
        with connection.cursor() as cursor:
            # TEHLİKELİ KOD - ASLA BÖYLE YAPMAYIN!
            query = f"""
                SELECT id, username, email, is_staff 
                FROM auth_user 
                WHERE username = '{username}' AND password = '{password_hash}'
            """
            
            print(f"[ZAFİYETLİ] Çalıştırılan sorgu: {query}")
            
            try:
                cursor.execute(query)
                user_data = cursor.fetchone()
                
                if user_data:
                    # Kullanıcı bulundu, session oluştur
                    request.session['user_id'] = user_data[0]
                    request.session['username'] = user_data[1]
                    request.session['is_admin'] = user_data[3]
                    
                    return redirect('/admin/')
                else:
                    error = 'Kullanıcı adı veya şifre yanlış.'
            except Exception as e:
                error = f'Hata oluştu: {str(e)}'
    
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



