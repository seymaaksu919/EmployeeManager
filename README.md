# EmployeeManager

Bu kodda , çalışanların bilgilerini saklamak ve yönetmek amacıyla basit bir sınıf tabanlı sistemdir. Python ile yazılmıştır ve temel olarak çalışan bilgilerini tutar, maaşlarını günceller ve çalışanların sayısını takip eder. Aynı zamanda her çalışan için maaş zammı yapabilme ve çalışan bilgilerini yazdırabilme gibi işlevlere sahiptir.

## Özellikler:
- Çalışan Bilgileri**: Çalışan adı, görev, maaş ve işe giriş tarihi gibi temel bilgileri saklar.
- Maaş Artışı**: Çalışanların maaşlarına belirli bir tutarda artış yapabilir.
- Toplam Çalışan Sayısı**: Sistemdeki toplam çalışan sayısını takip eder.
- Çalışan Bilgilerini Yazdırma**: Çalışan bilgilerini ekrana yazdırma işlevi.

## Kullanım:
Bu projeyi kullanarak çalışan bilgilerini ekleyebilir, her çalışan için maaş artışı yapabilir ve toplam çalışan sayısını görebilirsiniz. 

### Çalışan Nesnesi Oluşturma:
Bir çalışan nesnesi oluşturulurken aşağıdaki bilgilere ihtiyaç vardır:
- İsim: Çalışanın adı.
- İşe Giriş Tarihi: Çalışanın işe başlama tarihi.
- Görev: Çalışanın görev unvanı.
- Maaş: Çalışanın maaşı.

### Fonksiyonlar:
1. Yazdirma(): Çalışanın tüm bilgilerini ekrana yazdırır.
2. Yeni_maas(zam_tutari): Çalışanın maaşına belirtilen tutarda artış yapar.

### Örnek Kullanım:

Calisan1 = Calisan("ALİ", "12-07-2023", "BARİSTA", 18500)
Calisan1.Yazdirma()
Calisan1.Yeni_maas(500)

Calisan2 = Calisan("AYŞE", "10-07-2024", "ŞEF", 20000)
Calisan2.Yazdirma()
Calisan2.Yeni_maas(10000)

### Araçlar
Python
Visual Studio
