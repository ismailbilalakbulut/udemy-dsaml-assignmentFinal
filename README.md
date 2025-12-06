# 📚 Öğrenci Başarı Tahmin Sistemi

Makine öğrenmesi modeli kullanarak öğrenci sınav puanlarını tahmin eden web uygulaması.

## 🎯 Proje Hakkında

Bu proje, öğrencilerin çeşitli yaşam alışkanlıklarını ve özelliklerini kullanarak sınav puanlarını tahmin eden bir **Gradient Boosting Regression** modelini içerir. FastAPI ile oluşturulmuş modern web arayüzü ile kolay kullanılabilir.

## 📋 Özellikler

- ✅ **Gerçek Zamanlı Tahmin**: Öğrenci verilerini girerek anlık sınav puanı tahmini
- ✅ **Saat Validasyonu**: Günlük saat toplamı 24'ü geçmemesini kontrol eder
- ✅ **Responsive Tasarım**: Tüm cihazlarda güzel görünüm
- ✅ **Koyu Tema**: Göz yormayan modern arayüz
- ✅ **Hata Yönetimi**: Kullanıcı dostu hata mesajları

## 📊 Model Metrikleri 🚀

Modelin eğitim verileri üzerinde elde ettiği performans metrikleri aşağıdadır:

| Metrik | Değer | Açıklama |
| :--- | :--- | :--- |
| **R² (Belirlilik Katsayısı)** | $0.88543$ | Modelin varyansın yaklaşık **%88.5'ini** açıkladığını gösterir. 1'e yakın olması, modelin verilere iyi oturduğunu belirtir. |
| **RMSE (Kök Ortalama Karesel Hata)** | $5.42013$ | Tahmin edilen puanlar ile gerçek puanlar arasındaki ortalama farkın standart sapmasıdır. **Düşük olması** tahminlerin gerçek değerlere yakın olduğunu gösterir. |

## 🚀 Kurulum

### 1. Gerekli Paketleri Yükle
```bash
pip install -r requirements.txt
```

Veya manuel olarak:
```bash
pip install fastapi uvicorn scikit-learn pandas joblib jinja2
```

### 2. Modeli Oluştur
```bash
python main.py
```

Bu komut `ogrenci_basari_modeli.pkl` dosyasını oluşturacaktır.

### 3. Uygulamayı Çalıştır
```bash
uvicorn app:app --reload
```

### 4. Web Sitesini Aç
Tarayıcınızda açın: **http://127.0.0.1:8000**

## 📁 Klasör Yapısı

```
task8/
├── main.py                          # Model eğitim dosyası
├── app.py                           # FastAPI uygulaması
├── student_habits_performance.csv   # Eğitim veri seti (gitignore'da)
├── ogrenci_basari_modeli.pkl        # Eğitilmiş model (gitignore'da)
├── templates/
│   └── index.html                   # Web arayüzü
└── README.md                        # Bu dosya
```

## 📊 Model Girdileri

### Sayısal Veriler
- **Yaş**: 15-25 arası
- **Günlük Çalışma Saati**: 0-8 saat
- **Sosyal Medya Saati**: 0-8 saat
- **Netflix Saati**: 0-8 saat
- **Uyku Saati**: 0-12 saat
- **Devam Oranı**: 0-100%
- **Egzersiz Sıklığı**: 0-7 (haftada kaç gün)
- **Mental Sağlık Puanı**: 1-10

### Kategorik Veriler
- **Cinsiyet**: Erkek / Kadın
- **Yarı Zamanlı İş**: Evet / Hayır
- **Diyet Kalitesi**: Kötü / İyi / Çok İyi
- **Parental Eğitim Seviyesi**: Lise / Lisans / Yüksek Lisans
- **İnternet Kalitesi**: Zayıf / Orta / İyi
- **Ders Dışı Aktiviteler**: Evet / Hayır

## ⚠️ Önemli Notlar

- **Saat Validasyonu**: Günlük saatlerin toplamı 24'ü geçemez
- **Puan Sınırı**: Tahmin edilen puan 100'ü geçerse 100 olarak gösterilir
- **Veri Seti**: `.csv` dosyası gitignore'da olduğu için proje klonlandığında modeli yeniden eğitmeniz gerekir

## 🔧 Teknolojiler

- **Backend**: FastAPI, Uvicorn
- **ML**: scikit-learn, pandas, joblib
- **Frontend**: HTML5, CSS3, JavaScript
- **Model**: Gradient Boosting Regressor

## 📝 Kullanım Örneği

1. Web sitesine erişin
2. Öğrenci bilgilerini doldurun
3. Tüm saatlerin toplamının 24'ü geçmediğini kontrol edin
4. "Tahmini Yap" butonuna tıklayın
5. Tahmin edilen sınav puanını görün 

## 🎓 Veri Seti

Model, [student_habits_performance.csv]([Dosya Yolu](https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance)) dosyasından öğrenci alışkanlıkları ve sınav puanları verilerine dayanarak eğitilmiştir.

## 📄 Lisans

Bu proje eğitim amaçlı oluşturulmuştur.
