# Financial Fraud Detection System

Bu proje, finansal işlem verilerinde makine öğrenmesi algoritmalarını kullanarak sahtecilik tespiti yapmayı amaçlayan kapsamlı bir sistemdir. Proje, veri analizi, model geliştirme ve web tabanlı kullanıcı arayüzü bileşenlerini içermektedir.

## 📊 Proje Özeti

- **Veri Seti**: 6.3 milyon+ finansal işlem kaydı (Kaggle Synthetic Financial Dataset)
- **Amaç**: Sahte finansal işlemleri otomatik olarak tespit etmek
- **En İyi Model**: XGBoost (F1-Score: ~90%, ROC-AUC: ~0.96)
- **Web Arayüzü**: Flask tabanlı interaktif dashboard

## 🛠️ Kullanılan Teknolojiler

- **Python 3.8+**
- **Machine Learning**: Scikit-learn, XGBoost
- **Veri İşleme**: Pandas, NumPy
- **Görselleştirme**: Matplotlib, Seaborn
- **Web Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript

## 📋 Gereksinimler

Aşağıdaki Python kütüphanelerini kurun:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn flask joblib imbalanced-learn
```

## 🚀 Kurulum ve Çalıştırma

### 1. Repository'yi Klonlayın
```bash
git clone https://github.com/SedefAlkan/finance_fraud_detection.git
cd finance_fraud_detection
```

### 2. Veri Setini İndirin ve Yerleştirin
1. [Kaggle Synthetic Financial Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1) linkinden `PS_20174392719_1491204439457_log.csv` dosyasını indirin
2. İndirilen CSV dosyasını projenin **ana klasörüne** kopyalayın
3. Dosya yapısı şöyle olmalıdır:
```
finance_fraud_detection/
├── PS_20174392719_1491204439457_log.csv  # 👈 Bu dosyayı buraya ekleyin
├── .vscode/
├── __pycache__/
├── templates/
├── README.md
├── app.py
└── data_preprocessing_ML.ipynb
```

### 4. Model Eğitimini Çalıştırın
⚠️ **Önemli**: Flask uygulamasını çalıştırmadan önce modelin eğitilmesi gereklidir!

```bash
# Jupyter Notebook ile model eğitimi
jupyter notebook data_preprocessing_ML.ipynb
```

Notebook'u çalıştırarak:
- Veri analizi ve görselleştirmelerini görün
- Modelleri eğitin ve karşılaştırın  
- En iyi modelin `best_model.pkl` olarak kaydedildiğinden emin olun

### 5. Flask Uygulamasını Başlatın
```bash
python app.py
```

Uygulama `http://localhost:5000` adresinde çalışacaktır.

## 📁 Proje Yapısı

```
finance_fraud_detection/
├── 📄 PS_20174392719_1491204439457_log.csv  # Ana veri seti
├── 📓 data_preprocessing_ML.ipynb           # Model geliştirme
├── 🐍 app.py                               # Flask web uygulaması
├── 🤖 best_model.pkl                       # Eğitilmiş model
├── 📁 .vscode/                             # VS Code ayarları
├── 📁 __pycache__/                         # Python cache
├── 📁 templates/
│   └── index.html                          # Ana sayfa
└── 📋 README.md                            # Bu dosya
```

## 🔍 Özellikler

### Veri Analizi
- Eksik veri analizi ve temizleme
- Kategorik değişken dönüşümleri
- Sınıf dengesizliği çözümleri (SMOTE, Undersampling)
- Kapsamlı görselleştirmeler

### Model Geliştirme
- **Random Forest**: Ensemble learning yaklaşımı
- **Logistic Regression**: Baseline model
- **XGBoost**: En yüksek performans gösteren model
- Hiperparametre optimizasyonu (GridSearchCV)
- Cross-validation ile model validasyonu

### Değerlendirme Metrikleri
- **Accuracy**: Genel doğruluk
- **Precision**: Pozitif tahminlerin doğruluğu
- **Recall**: Gerçek pozitifleri yakalama oranı
- **F1-Score**: Precision ve Recall'un harmonik ortalaması
- **ROC-AUC**: Model ayırt etme kabiliyeti
- **Confusion Matrix**: Detaylı hata analizi

### Web Arayüzü
- CSV dosyası yükleme özelliği
- Gerçek zamanlı fraud analizi
- Risk skorlama sistemi
- Renk kodlu sonuç görselleştirme (🔴 Riskli, 🟢 Güvenli)
- Kullanıcı dostu arayüz

## 📈 Model Performansı

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|---------|----------|---------|
| Random Forest | 0.889531 | 0.898506 | 0.878271 | 0.888273 | 0.959157 |
| Logistic Regression | 0.838405 | 0.812360 | 0.880097 | 0.844873 | 0.923006 |
| **XGBoost** | **0.905965** | **0.913259** | **0.897139** | **0.905127** | **0.966125** |

## 🎯 Kullanım Senaryoları

1. **Bankalar**: Gerçek zamanlı işlem izleme
2. **E-ticaret**: Şüpheli ödeme tespiti  
3. **Fintech**: Risk değerlendirme sistemleri
4. **Araştırma**: Fraud detection algoritma karşılaştırmaları




