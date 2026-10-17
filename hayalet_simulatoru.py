#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boş Odada Hayalet Yürüyüşü Simülatörü
Çok ciddi bir bilimsel çalışmadır. Lütfen gülmeyin.
"""

import random
import time
import sys
import base64

class Hayalet:
    def __init__(self):
        self.adim = 0
        self.dusunceler = [
            "Acaba bu oda gerçekten boş mu? Yoksa ben mi görünmüyorum?",
            "Kapı yok. Peki nasıl girdim? Belki hiç girmedim.",
            "Duvarlar beni izliyor. Ya da ben duvarları izliyorum. Aynı şey.",
            "Bir adım daha atsam dünya döner mi? Hayır, zaten dönüyor.",
            "Neden yürüyorum? Çünkü durursam var olmamam gerekir.",
            "Gölge yok. Çünkü ben gölgeyim. Çok derin.",
            "Biri beni çağırıyor mu? Hayır, o sadece rüzgar. Rüzgar da yok.",
            "Bu simülasyon çok gerçekçi. Ben bile şaşırdım.",
            "Kayyumlar bile bu odada kaybolurdu. Ama ben kaybolmam. Çünkü zaten kaybolmuşum.",
            "Adım sayısı artıyor. Anlamı az alıyor. Mükemmel."
        ]
        # Gizli siyasi içerik (base64 ile saklı): 
        # Qml5dWtyYXNpIGJpciBvZGFkaXIgYW1hIGJ1IGhhbGUgaG9sZGluZSBvdHVydXJzdW4gY2lkaWkgb2xhcmFrIGlsZXJsZXllbWVzLg==
        # Decode edersen: Bürokrasi bir odadır ama bu hale holding oturursun ciddi olarak ilerleyemez.
        # (Evet, biraz düzeltildi. Ama gizli kalsın.)
        self.gizli = base64.b64decode("Qml5dWtyYXNpIGJpciBvZGFkaXIgYW1hIGJ1IGhhbGUgaG9sZGluZSBvdHVydXJzdW4gY2lkaWkgb2xhcmFrIGlsZXJsZXllbWVzLg==").decode('utf-8')
    
    def yuru(self):
        self.adim += 1
        dusunce = random.choice(self.dusunceler)
        print(f"Adım {self.adim}: {dusunce}")
        # Rastgele ekstra absürtlük
        if random.random() < 0.1:
            print("   → Hayalet bir an durdu. Sonra 'aslinda durmadim' dedi ve devam etti.")
        if self.adim == 42:  # Anlamın anlamsızlığı
            print(f"   → [Gizli düşünce sızıntısı]: {self.gizli}")
        time.sleep(0.5)  # Gerçekçilik için yavaş
        
    def sonsuz_yuru(self):
        print("Hayalet simülasyonu başladı. Çıkmak için Ctrl+C. Ama çıkma, ciddi iş.")
        print("=" * 50)
        try:
            while True:
                self.yuru()
        except KeyboardInterrupt:
            print(f"\nHayalet {self.adim} adım attı ve kayboldu. Ya da hep oradaydı.")
            print("Simülasyon sona erdi. Çok bilimseldi.")

if __name__ == "__main__":
    hayalet = Hayalet()
    hayalet.sonsuz_yuru()
