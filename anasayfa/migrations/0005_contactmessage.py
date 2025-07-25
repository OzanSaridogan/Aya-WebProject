# Generated by Django 5.2.4 on 2025-07-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0004_ayasbilgi'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad Soyad')),
                ('email', models.EmailField(max_length=254, verbose_name='E-posta')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
