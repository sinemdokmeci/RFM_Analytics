# RFM ile Müşteri Segmantasyonu

### 1. İş Problemi (Business Problem)
# Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# 01/12/2010 and 09/12/2011 tarihleri arasındaki satışlarını içeriyor

### 2. Veriyi Anlama (Data Understanding)
import datetime as dt
import pandas as pd
from datetime import timedelta
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
df_ = pd.read_csv("/Users/sinemdokmeci/PycharmProjects/CRM_E-Ticaret/dataset/Online Retail Data - Year 2009-2010-2011.csv")
df = df_.copy()
df.head()
df.shape
#Ürün sayımıza bakalım.
df["Description"].nunique()
#Her bir ürün kaç farklı faturada satılmış
df["Description"].value_counts().head()
#Ürünlerden kaç adet satılmış
df.groupby("Description").agg({"Quantity": "sum"}).head()
#Her bir üründen toplam ne kadar sipariş verilmiş miktarını hesaplıyoruz
df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head()
#Toplam kaç tane fatura kesildi
df["Invoice"].nunique()
#satış başına toplam kazanç
df["TotalPrice"] = df["Quantity"] * df["Price"]
#faturalarda ki satışların toplamı
df.groupby("Invoice").agg({"TotalPrice": "sum"}).head()
### 3. Veri Hazırlama (Data Preparation)
#Eksik verileri silme
df.isnull().sum()
df.describe().T
df = df[(df['Quantity'] > 0)]
df.dropna(inplace=True)
df.head()
#Değişken tiplerimize bakalım datetime olması gereken tarih değişkenlerini düzeltelim
print(df.dtypes)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M', errors='coerce')
#Analiz tarihi belirleyelim
a = df["InvoiceDate"].max()
today_date = a + pd.Timedelta(days=2)
#RFM verilerini oluşturalım
rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     'Invoice': lambda Invoice: Invoice.nunique(),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})
rfm.head()

#Değişken isimlerini değiştirelim
rfm.columns = ['recency', 'frequency', 'monetary']
#Monatary değişkenini kontrol edelim
rfm = rfm[rfm["monetary"] > 0]
rfm.shape

### 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
#R ters F,M düz büyüklük küçüklük algısı yapmamız lazım
#qcut fonksiyonu ile çeyrek değerlere göre bölme işlemi yaparız
# 0-100, 0-20, 20-40, 40-60, 60-80, 80-100 gibi büyükten küçüğe sıralayıp böler
#iyiolana 5 kötü olana 1
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])
#RFM Skore değişkeni hesaaplarız R ve F ile yapılır
rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))
rfm.describe().T
rfm[rfm["RFM_SCORE"] == "55"] # en değerli müşterler için
rfm[rfm["RFM_SCORE"] == "11"] # Daha az değerli olanlar için


### 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
# Segment Listesi
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

#skorları birleştirme isimlendirme
rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
# segmentleri inceleyelim
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

#bizden kaybedilecek müşterileri (new_customers) istendiğinde
new_df = pd.DataFrame()
new_df["new_customer_id"] = rfm[rfm["segment"] == "new_customers"].index
new_df["new_customer_id"] = new_df["new_customer_id"].astype(int)
new_df.to_csv("new_customers.csv")
rfm.to_csv("rfm.csv")