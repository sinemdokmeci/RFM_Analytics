# RFM_Analytics
In CRM analysis, we will perform RFM calculations to create valuable customer segments by evaluating the recency of the last purchase, purchase frequency, and total spending amount.

# 1. İş Problemi (Business Problem)
Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
01/12/2010 and 09/12/2011 tarihleri arasındaki satışlarını içeriyor

# Veri Seti Hikayesi
Bu veri seti, bir e-ticaret firmasında ki müşterilerin demografik bilgileri ve alışveriş davranışlarını içermektedir. Müşterilerin yaşları, medeni durumları, gelir düzeyleri ve çocuk sahibi olup olmadıkları gibi özellikler yer almakta. Ayrıca, müşterilerin mağazaya ne zaman kaydoldukları, son alışverişlerinin üzerinden geçen süre ve toplam harcamaları ile sipariş sayıları da bulunmaktadır.

# Veriseti Hakkında
ID: Müşterinin benzersiz kimlik numarası.
Year_Birth: Müşterinin doğum yılı.
Education: Müşterinin eğitim seviyesi (örneğin, lisans, yüksek lisans, doktora).
Marital_Status: Müşterinin medeni durumu (örneğin, evli, bekar, birlikte).
Income: Müşterinin yıllık geliri.
Kidhome: Müşterinin evinde yaşayan küçük çocuk sayısı.
Teenhome: Müşterinin evinde yaşayan genç (13-19 yaş arası) sayısı.
Dt_Customer: Müşterinin kayıt olduğu tarih.
Recency: Müşterinin son alışverişinin üzerinden geçen gün sayısı.
customer_value_total: Müşterinin bugüne kadar yaptığı toplam harcama.
order_num_total: Müşterinin bugüne kadar verdiği sipariş sayısı.

# Projenin Aşamaları

1. Veriyi Anlama (Data Understanding)
İlk aşamada, elimizdeki veriyi inceleyip anlayacağız. Müşterilere ait demografik bilgiler, alışveriş geçmişi ve harcamalar gibi verilerin ne anlama geldiğini analiz edeceğiz. Eksik veya tutarsız veriler olup olmadığını kontrol edeceğiz ve verinin genel yapısını gözden geçireceğiz.

2. Veri Hazırlama (Data Preparation)
Bu aşamada, veriyi analiz edilebilir hale getireceğiz. Eksik veya hatalı verileri temizleyeceğiz, aykırı değerleri düzelteceğiz. Gerekirse yeni öznitelikler oluşturacağız ve veriyi modelleme için uygun bir yapıya sokacağız. Ayrıca, veriyi RFM skorlaması için hazır hale getireceğiz.

3. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
RFM analizi yapabilmek için müşterilerin Recency (son alışveriş zamanı), Frequency (alışveriş sıklığı) ve Monetary (toplam harcama tutarı) skorlarını hesaplayacağız. Bu adımda, veriyi gruplandırarak her müşteriye bu üç metrik üzerinden puanlar vereceğiz. Skorları hesapladıktan sonra her müşteri belirli bir RFM değerine sahip olacak.

4. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
Son olarak, RFM skorlarına göre müşterileri segmentlere ayıracağız. Örneğin, yüksek skor alanları "en değerli müşteriler" olarak belirleyeceğiz, düşük skor alanları ise "yeniden kazanılması gereken müşteriler" olarak sınıflandıracağız. Bu segmentleri analiz edip, her bir gruba yönelik pazarlama stratejileri ve aksiyon planları oluşturacağız.
