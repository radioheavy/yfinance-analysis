# 📊 yfinance Veri Yapısı ve Kaynakları

## 1. Temel Veriler
### 1.1 Şirket Bilgileri (`info`)
- 🏢 Şirket Adı (`longName`)
- 🏭 Sektör (`sector`)
- 🏗️ Endüstri (`industry`)
- 📝 İş Açıklaması (`longBusinessSummary`)

### 1.2 Piyasa Verileri (`info`)
- 💰 Güncel Fiyat (`currentPrice`)
- 🎯 Hedef Fiyat (`targetMeanPrice`)
- 📈 Piyasa Değeri (`marketCap`)
- 🔢 Hisse Sayısı (`sharesOutstanding`)

### 1.3 Haberler (`get_news()`)
- 📰 Başlık
- 📅 Tarih
- 🔍 Kaynak
- 🔗 Link
- 📄 Özet

## 2. Finansal Veriler
### 2.1 Gelir Tablosu
- 📊 Yıllık (`income_stmt`)
  - Toplam Gelir
  - Faaliyet Giderleri
  - Net Kar
  - EPS
- 📈 Çeyreklik (`quarterly_income_stmt`)
  - Son 4 çeyrek verileri
  - Karşılaştırmalı büyüme

### 2.2 Bilanço
- 📑 Yıllık (`balance_sheet`)
  - Varlıklar
  - Yükümlülükler
  - Özsermaye
- 📋 Çeyreklik (`quarterly_balance_sheet`)
  - Dönemsel değişimler
  - Likidite durumu

### 2.3 Nakit Akışı
- 💵 Yıllık (`cashflow`)
  - İşletme faaliyetleri
  - Yatırım faaliyetleri
  - Finansman faaliyetleri
- 💸 Çeyreklik (`quarterly_cashflow`)
  - Serbest nakit akışı
  - Temettü ödemeleri

### 2.4 Finansal Oranlar (`info`)
#### Değerleme Oranları
- 📊 F/K (`trailingPE`)
- 📈 İleriye Dönük F/K (`forwardPE`)
- 📉 PEG (`pegRatio`)
- 📊 F/S (`priceToSalesTrailing12Months`)
- 📑 F/DD (`priceToBook`)

#### Karlılık Oranları
- 💰 Brüt Marj (`grossMargins`)
- 💵 FAVÖK Marjı (`ebitdaMargins`)
- 💸 Faaliyet Marjı (`operatingMargins`)
- 📈 ROE (`returnOnEquity`)
- 📊 ROA (`returnOnAssets`)

#### Büyüme Oranları
- 📈 Gelir Büyümesi (`revenueGrowth`)
- 📊 Kazanç Büyümesi (`earningsGrowth`)
- 📉 Hisse Başı Kar Büyümesi (`earningsQuarterlyGrowth`)

## 3. Teknik Veriler
### 3.1 Fiyat Geçmişi (`history()`)
- 📈 Açılış/Kapanış Fiyatları
- 📊 Yüksek/Düşük Fiyatlar
- 📉 İşlem Hacmi
- 📅 Tarihsel Veriler
  - Günlük
  - Haftalık
  - Aylık
  - Yıllık

### 3.2 Teknik Göstergeler (Hesaplanan)
- 📈 50 Günlük Hareketli Ortalama
- 📉 200 Günlük Hareketli Ortalama
- 📊 RSI (Göreceli Güç Endeksi)

## 4. Kurumsal Veriler
### 4.1 Büyük Hissedarlar (`major_holders`)
- 👥 İçeriden Sahiplik Oranı
- 🏢 Kurumsal Sahiplik Oranı
- 📊 Halka Açık Hisse Oranı
- 📈 Toplam Kurum Sayısı

### 4.2 Kurumsal Yatırımcılar (`institutional_holders`)
- 🏢 Kurum Adı
- 📊 Sahiplik Oranı
- 💰 Hisse Sayısı
- 📈 Değişim Yüzdesi
- 📅 Raporlama Tarihi

## 5. Diğer Veriler
### 5.1 Sürdürülebilirlik (`sustainability`)
- 🌍 Toplam ESG Skoru
- 🌱 Çevresel Skor
- 👥 Sosyal Skor
- 📊 Yönetişim Skoru
- 🏢 Sektör Karşılaştırmaları

### 5.2 Opsiyon Verileri
- 📅 Vade Tarihleri (`options`)
- 📈 Call Opsiyonları (`option_chain()`)
  - Strike Fiyatları
  - Hacim
  - Açık Pozisyonlar
- 📉 Put Opsiyonları (`option_chain()`)
  - Strike Fiyatları
  - Hacim
  - Açık Pozisyonlar

### 5.3 Kazanç Bilgileri
- 📊 Kazanç Tarihleri (`earnings_dates`)
- 📈 EPS Tahminleri
- 📉 Gerçekleşen EPS
- 💹 Sürpriz Yüzdeleri
- 📅 Gelecek Kazanç Tarihleri

## 6. Veri Güncelleme Sıklığı
- ⚡ Gerçek Zamanlı Veriler
  - Fiyat
  - Hacim
  - Temel Piyasa Verileri
- 📅 Günlük Güncellenen Veriler
  - Finansal Oranlar
  - Teknik Göstergeler
- 📊 Periyodik Güncellenen Veriler
  - Finansal Tablolar (Çeyreklik)
  - Kurumsal Sahiplik (3 Aylık)
  - ESG Skorları (Yıllık)