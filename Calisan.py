#Çalışan adında sınıf oluşturulur.
class Calisan:       
    
     #Başlangınçtaki çalışsan sayısı sıfır kabul edilir.
    toplam_calisan_sayisi=0          

    #Çalışan sınıfının özellikleri
    def __init__(self, isim, ise_giris_tarihi, gorevi, maas):
        self.isim = isim
        self.ise_giris_tarihi = ise_giris_tarihi
        self.gorevi = gorevi
        self.maas = maas
        Calisan.toplam_calisan_sayisi += 1


    # Burada 'self' ile nesnenin bilgilerine erişilir ve ekrana yazdırılır.
    def Yazdirma(self):
        print(f"İsim: {self.isim}, Görev: {self.gorevi}, Maaş: {self.maas}, İse Giriş Tarihi: {self.ise_giris_tarihi}")


    #Yeni maas oranının hesaplanması
    def Yeni_maas(self, zam_tutari):
     self.maas += zam_tutari
     print("Yeni maaş:", self.maas)




# Çalışan nesnesi oluşturuluyor
Calisan1 = Calisan("ALİ", "12-07-2023", "BARİSTA", 18500)
Calisan1.Yazdirma()
Calisan1.Yeni_maas(500)

Calisan2 = Calisan("AYŞE","10-07-2024","ŞEF",20000)
Calisan2.Yazdirma()
Calisan2.Yeni_maas(10000)



