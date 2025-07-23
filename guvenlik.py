import os
from datetime import datetime
import pyautogui

# Ayarlar
SIFRE = "1234"  # Kendi şifreni yaz
MAX_DENEME = 3
KAYIT_KLASORU = os.path.expanduser("~/Desktop/ekran_guvenlik/kayitlar")

# Klasörü oluştur
if not os.path.exists(KAYIT_KLASORU):
    os.makedirs(KAYIT_KLASORU)

deneme_sayisi = 0

while True:
    girilen = input("Şifreyi girin: ")
    
    if girilen == SIFRE:
        print("Giriş başarılı!")
        break
    else:
        deneme_sayisi += 1
        print(f"Yanlış şifre! Kalan deneme: {MAX_DENEME - deneme_sayisi}")
        
        if deneme_sayisi >= MAX_DENEME:
            tarih = datetime.now().strftime("%d%m%Y_%H%M%S")
            dosya_yolu = os.path.join(KAYIT_KLASORU, f"hata_{tarih}.png")
            pyautogui.screenshot(dosya_yolu)
            print(f"3 kez hata! Ekran kaydedildi: {dosya_yolu}")
            deneme_sayisi = 0