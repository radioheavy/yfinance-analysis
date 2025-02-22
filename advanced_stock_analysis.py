import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns
from tabulate import tabulate

def get_stock_info(symbol):
    """
    Hisse senedi hakkında tüm temel bilgileri getirir
    """
    print(f"\n{symbol} TEMEL BİLGİLER:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    info = stock.info
    
    # Temel Bilgiler
    print("\n1. ŞİRKET BİLGİLERİ:")
    print(f"Şirket Adı: {info.get('longName', 'Veri yok')}")
    print(f"Sektör: {info.get('sector', 'Veri yok')}")
    print(f"Endüstri: {info.get('industry', 'Veri yok')}")
    print(f"Açıklama: {info.get('longBusinessSummary', 'Veri yok')}")
    
    # Piyasa Bilgileri
    print("\n2. PİYASA BİLGİLERİ:")
    print(f"Güncel Fiyat: ${info.get('currentPrice', 'Veri yok')}")
    print(f"Hedef Fiyat: ${info.get('targetMeanPrice', 'Veri yok')}")
    print(f"Piyasa Değeri: ${info.get('marketCap', 'Veri yok'):,.2f}")
    print(f"Hisse Sayısı: {info.get('sharesOutstanding', 'Veri yok'):,.0f}")

def get_stock_news(symbol):
    """
    Hisse senedi ile ilgili son haberleri getirir
    """
    print(f"\n{symbol} HABERLER:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    try:
        # Yeni haber alma yöntemi
        news = stock.get_news()
        
        if news and len(news) > 0:
            for i, article in enumerate(news[:5], 1):
                print(f"\n{i}. HABER:")
                print(f"Başlık: {article.get('title', 'Başlık yok')}")
                
                publish_time = article.get('providerPublishTime', 0)
                if publish_time:
                    date = datetime.fromtimestamp(publish_time)
                    print(f"Tarih: {date.strftime('%Y-%m-%d %H:%M')}")
                
                print(f"Kaynak: {article.get('publisher', 'Kaynak belirtilmemiş')}")
                print(f"Link: {article.get('link', 'Link yok')}")
                
                if 'summary' in article:
                    print(f"Özet: {article['summary'][:200]}...")
        else:
            print("Haber verisi bulunamadı.")
    except Exception as e:
        print(f"Haber verisi alınırken hata oluştu: {str(e)}")

def get_financial_statements(symbol):
    """
    Tüm finansal tabloları getirir
    """
    print(f"\n{symbol} FİNANSAL TABLOLAR:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    
    # Gelir Tablosu
    print("\n1. GELİR TABLOSU (YILLIK):")
    print(stock.income_stmt)
    
    print("\n2. GELİR TABLOSU (ÇEYREK):")
    print(stock.quarterly_income_stmt)
    
    # Bilanço
    print("\n3. BİLANÇO (YILLIK):")
    print(stock.balance_sheet)
    
    print("\n4. BİLANÇO (ÇEYREK):")
    print(stock.quarterly_balance_sheet)
    
    # Nakit Akışı
    print("\n5. NAKİT AKIŞI (YILLIK):")
    print(stock.cashflow)
    
    print("\n6. NAKİT AKIŞI (ÇEYREK):")
    print(stock.quarterly_cashflow)

def get_detailed_ratios(symbol):
    """
    Tüm finansal oranları getirir
    """
    print(f"\n{symbol} FİNANSAL ORANLAR:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    info = stock.info
    
    ratios = {
        'Değerleme Oranları': {
            'F/K': info.get('trailingPE', 'Veri yok'),
            'İleriye Dönük F/K': info.get('forwardPE', 'Veri yok'),
            'PEG': info.get('pegRatio', 'Veri yok'),
            'F/S': info.get('priceToSalesTrailing12Months', 'Veri yok'),
            'F/DD': info.get('priceToBook', 'Veri yok')
        },
        'Karlılık Oranları': {
            'Brüt Marj': info.get('grossMargins', 'Veri yok'),
            'FAVÖK Marjı': info.get('ebitdaMargins', 'Veri yok'),
            'Faaliyet Marjı': info.get('operatingMargins', 'Veri yok'),
            'Net Marj': info.get('profitMargins', 'Veri yok'),
            'ROE': info.get('returnOnEquity', 'Veri yok'),
            'ROA': info.get('returnOnAssets', 'Veri yok')
        },
        'Büyüme Oranları': {
            'Gelir Büyümesi': info.get('revenueGrowth', 'Veri yok'),
            'Kazanç Büyümesi': info.get('earningsGrowth', 'Veri yok'),
            'Hisse Başı Kar Büyümesi': info.get('earningsQuarterlyGrowth', 'Veri yok')
        }
    }
    
    for category, category_ratios in ratios.items():
        print(f"\n{category}:")
        print(tabulate([(k, v) for k, v in category_ratios.items()], headers=['Oran', 'Değer']))

def get_technical_indicators(symbol):
    """
    Teknik göstergeleri hesaplar ve getirir
    """
    print(f"\n{symbol} TEKNİK GÖSTERGELER:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    hist = stock.history(period='1y')
    
    # Hareketli Ortalamalar
    hist['MA50'] = hist['Close'].rolling(window=50).mean()
    hist['MA200'] = hist['Close'].rolling(window=200).mean()
    
    # RSI
    delta = hist['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    hist['RSI'] = 100 - (100 / (1 + rs))
    
    print("\nSon Teknik Göstergeler:")
    print(f"50 Günlük Hareketli Ortalama: ${hist['MA50'].iloc[-1]:.2f}")
    print(f"200 Günlük Hareketli Ortalama: ${hist['MA200'].iloc[-1]:.2f}")
    print(f"RSI (14 gün): {hist['RSI'].iloc[-1]:.2f}")

def get_institutional_holders(symbol):
    """
    Kurumsal yatırımcı bilgilerini getirir
    """
    print(f"\n{symbol} KURUMSAL YATIRIMCILAR:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    
    print("\n1. BÜYÜK HİSSEDARLAR:")
    print(stock.major_holders)
    
    print("\n2. KURUMSAL YATIRIMCILAR:")
    print(stock.institutional_holders)

def get_earnings_info(symbol):
    """
    Kazanç bilgilerini getirir
    """
    print(f"\n{symbol} KAZANÇ BİLGİLERİ:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    
    # Kazanç Tarihleri ve Tahminler
    print("\n1. KAZANÇ TAHMİNLERİ VE GEÇMİŞİ:")
    try:
        earnings_dates = stock.earnings_dates
        if earnings_dates is not None and not earnings_dates.empty:
            print(tabulate(earnings_dates, headers='keys', tablefmt='grid'))
        else:
            print("Kazanç tarihi verisi bulunamadı.")
    except:
        print("Kazanç tarihi verisi alınırken hata oluştu.")
    
    # Gelecek Kazanç Tarihleri
    print("\n2. GELECEK KAZANÇ TARİHLERİ:")
    try:
        calendar = stock.calendar
        if calendar is not None and not calendar.empty:
            print(tabulate(calendar, headers='keys', tablefmt='grid'))
        else:
            print("Takvim verisi bulunamadı.")
    except:
        print("Takvim verisi alınırken hata oluştu.")
    
    # Analist Tahminleri
    print("\n3. ANALİST TAHMİNLERİ:")
    try:
        recommendations = stock.recommendations
        if recommendations is not None and not recommendations.empty:
            recent_recommendations = recommendations.tail(5)
            print(tabulate(recent_recommendations, headers='keys', tablefmt='grid'))
        else:
            print("Analist tahmini bulunamadı.")
    except:
        print("Analist tahminleri alınırken hata oluştu.")

def get_options_data(symbol):
    """
    Opsiyon verilerini getirir
    """
    print(f"\n{symbol} OPSİYON VERİLERİ:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    
    print("\nMevcut Opsiyon Vadeleri:")
    print(stock.options)
    
    if len(stock.options) > 0:
        expiry = stock.options[0]
        opt = stock.option_chain(expiry)
        
        print(f"\nİlk Vade ({expiry}) için Opsiyon Zinciri:")
        print("\nCALL Opsiyonları:")
        print(opt.calls.head())
        print("\nPUT Opsiyonları:")
        print(opt.puts.head())

def get_sustainability_score(symbol):
    """
    Sürdürülebilirlik skorlarını getirir
    """
    print(f"\n{symbol} SÜRDÜRÜLEBİLİRLİK SKORLARI:")
    print("-" * 50)
    
    stock = yf.Ticker(symbol)
    print(stock.sustainability)

def analyze_multiple_stocks(symbols, period='1y'):
    """
    Birden fazla hisse senedini karşılaştırmalı analiz eder
    """
    print("\nÇOKLU HİSSE SENEDİ ANALİZİ:")
    print("-" * 50)
    
    try:
        # Fiyat verilerini çek
        data = yf.download(symbols, period=period, auto_adjust=True)['Close']
        
        # Normalize et
        normalized_data = data.div(data.iloc[0]).mul(100)
        
        # Grafik
        plt.figure(figsize=(15, 7))
        for symbol in symbols:
            plt.plot(normalized_data.index, normalized_data[symbol], label=symbol)
        
        plt.title("Karşılaştırmalı Performans Analizi (Başlangıç=100)")
        plt.xlabel("Tarih")
        plt.ylabel("Normalize Edilmiş Değer")
        plt.legend()
        plt.grid(True)
        plt.savefig("karsilastirma_grafik.png")
        plt.close()
        
        # Karşılaştırma tablosu
        comparison_data = []
        for symbol in symbols:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            # Temettü verisini düzelt
            dividend_yield = info.get('dividendYield', 0)
            if dividend_yield:
                dividend_yield = round(dividend_yield * 100, 2)
            
            comparison_data.append({
                'Hisse': symbol,
                'Fiyat': info.get('currentPrice', 'Veri yok'),
                'Piyasa Değeri (M)': info.get('marketCap', 0) / 1e9,
                'F/K': info.get('trailingPE', 'Veri yok'),
                'Beta': info.get('beta', 'Veri yok'),
                'Temettü (%)': dividend_yield if dividend_yield else 'Veri yok'
            })
        
        print("\nKarşılaştırma Tablosu:")
        print(tabulate(comparison_data, headers='keys', tablefmt='grid'))
        
    except Exception as e:
        print(f"Hata: {str(e)}")
        print("Karşılaştırmalı analiz yapılırken bir hata oluştu.")

def get_fund_data(symbol):
    """
    Yatırım fonu verilerini getirir
    """
    print(f"\n{symbol} FON VERİLERİ:")
    print("-" * 50)
    
    fund = yf.Ticker(symbol)
    
    try:
        # Temel fon bilgileri
        info = fund.info
        print("\nFon Bilgileri:")
        print(f"Fon Adı: {info.get('shortName', 'Veri yok')}")
        print(f"Kategori: {info.get('category', info.get('fundFamily', 'Veri yok'))}")
        print(f"Açıklama: {info.get('longBusinessSummary', 'Veri yok')}")
        
        # Performans metrikleri
        print("\nPerformans Metrikleri:")
        print(f"YTD Getiri: %{info.get('ytdReturn', 'Veri yok')}")
        print(f"3 Yıllık Getiri: %{info.get('threeYearAverageReturn', 'Veri yok')}")
        print(f"5 Yıllık Getiri: %{info.get('fiveYearAverageReturn', 'Veri yok')}")
        
        # Risk metrikleri
        print("\nRisk Metrikleri:")
        print(f"Beta: {info.get('beta', 'Veri yok')}")
        print(f"Standart Sapma: {info.get('standardDeviation', 'Veri yok')}")
        print(f"Sharpe Oranı: {info.get('morningStarRiskRating', 'Veri yok')}")
        
        # Portföy dağılımı
        print("\nPortföy Dağılımı:")
        holdings = fund.get_holdings() if hasattr(fund, 'get_holdings') else None
        if holdings is not None and not holdings.empty:
            print(holdings.head(10))
        else:
            print("Portföy dağılımı verisi bulunamadı.")
            
    except Exception as e:
        print(f"Hata: {str(e)}")

def main():
    # Ana hisse senedi analizi
    symbol = "AAPL"
    print(f"\n{symbol} HİSSESİ İÇİN KAPSAMLI ANALİZ BAŞLIYOR...")
    
    # Tüm analizleri çalıştır
    get_stock_info(symbol)
    get_stock_news(symbol)
    get_financial_statements(symbol)
    get_detailed_ratios(symbol)
    get_technical_indicators(symbol)
    get_institutional_holders(symbol)
    get_earnings_info(symbol)
    get_options_data(symbol)
    get_sustainability_score(symbol)
    
    # Çoklu hisse analizi
    symbols = ["AAPL", "MSFT", "GOOGL"]
    analyze_multiple_stocks(symbols)
    
    # Fon analizi
    print("\nFON ANALİZİ ÖRNEĞİ (SPY ETF):")
    get_fund_data("SPY")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nHata: {str(e)}")