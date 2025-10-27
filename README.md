#  Projenin Amacı

Bu projenin temel amacı, gerçek dünyadan alınan görüntü veya videoları **Pixar tarzı bir animasyon stiline dönüştürebilen** özgün ve geliştirilebilir bir yapay zeka sistemi inşa etmektir. 

Mevcut hazır modellerin sınırlı özelleştirme imkânları nedeniyle, proje kapsamında bir temel difüzyon modelinin (**Stable Diffusion**) üzerine **LoRA (Low-Rank Adaptation)** yöntemiyle özel bir tarz transferi eğitimi gerçekleştirilerek, kişiye veya stile özel ince ayar (**fine-tune**) edilmiş bir model oluşturulacaktır.

---

##  Proje Açıklaması

Proje süreci aşağıdaki temel adımları kapsamaktadır:

### 1. Veri Hazırlığı

Pixar tarzına uygun görsellerden oluşan küçük boyutlu bir veri kümesi hazırlanmakta ve bu görseller üzerinde **altyazılar (prompt/caption)** üretilmektedir.

### 2. Altyapı Kurulumu

- Eğitim ortamı olarak **kohya_ss** GUI tabanlı framework seçilmiştir.  
- Gerekli bağımlılıklarla birlikte yerel bir **Python sanal ortamı** oluşturulmuştur.  
- Eğitim işlemi, kullanıcının bilgisayarında **güvenli ve offline** olarak gerçekleştirilmektedir.

### 3. Model Eğitimi (LoRA)

- Eğitimde, **Stable Diffusion** mimarisine dayalı bir temel model üzerine, düşük kaynak tüketimli **LoRA** yöntemi kullanılır.  
- Bu yöntemle modelin tüm ağırlıkları değiştirilmeden, yalnızca seçili katmanlara küçük güncellemeler uygulanır.  
- Böylece eğitim süreci hızlı, hafif ve kişiselleştirilebilir hale gelir.

### 4. Modelin Kullanımı

- Elde edilen yeni model, **Stable Diffusion WebUI** arayüzü ile görsel üretim amacıyla kullanılır.  
- Verilen herhangi bir gerçek görüntü, “**Pixar tarzı**”na benzer şekilde **stilize edilir**.

---
---

##  Veri Seti Özeti

Bu projede sabit bir dış veri seti kullanılmamıştır. Bunun yerine kullanıcı tarafından belirlenen bir `.mp4` formatındaki video, `ffmpeg` komutu aracılığıyla karelerine ayrılarak özel bir görsel veri seti oluşturulmuştur.

- **Kaynak:** `input_videos/video.mp4`  
- **Veri Tipi:** Kare görseller (`.png`)  
- **Toplam Görsel Sayısı:** Yaklaşık 210 kare (30 FPS × 7 saniye)  
- **Karelerin Konumu:** `input_images/` klasörü  
- **Dönüştürülmüş Çıktılar:** `styled_frames/` klasöründe yer almaktadır  
- **Veri Etiketleme:** Etiketli veri bulunmamaktadır (unsupervised)  
- **Kullanım Amacı:** Her kareyi tek tek Pixar tarzında dönüştürmek için girdi olarak kullanılır
- LoRa kullanımında 210 adet veri gayet idealdir
---

##  Yöntemin Tercih Sebepleri

- **LoRA**, düşük GPU belleği ile eğitime olanak tanır, kullanıcı dostudur.  
- Eğitim sürecine müdahale imkanı sunar; bu sayede proje sadece “hazır modelle üretim” değil, **model geliştirme** projesidir.  
- Eğitimler yerel bilgisayarda yapıldığından **veri gizliliği korunur**.  
- Sonuçlar hem **akademik** hem de **yaratıcı projeler** için yüksek potansiyel taşır.

---

>  Bu proje, hem teknik öğrenim hem de yaratıcı üretim süreçlerine katkı sağlayan açık uçlu bir yapay zeka uygulamasıdır.

## Pixar Görsel Karşılaştırmaları

<table>
  <tr>
    <td align="center"><img src="example_outputs/input1.jpg" width="300"/></td>
    <td align="center"><img src="example_outputs/output1.jpg" width="300"/></td>
  </tr>
  <tr>
    <td align="center"><img src="example_outputs/input2.jpg" width="300"/></td>
    <td align="center"><img src="example_outputs/output2.jpg" width="300"/></td>
  </tr>
</table>

---

##  Örnek Videolar

- [ Video 1](example_outputs/result1.mp4)  
- [ Video 2](example_outputs/result2.mp4)


---

##  Performans Metrikleri


###  LPIPS Kalite Değerlendirme

| Görsel         | LPIPS Skoru |
|----------------|--------------|
| `input1.jpg`   | 0.4892       |
| `input2.jpg`   | 0.5880       |
| **Ortalama**   | **0.5386**   |

> Görsel kalitenin değerlendirilmesi için **LPIPS (Learned Perceptual Image Patch Similarity)** metriği kullanılmıştır.  
> Stilize edilen görsellerin orijinallerine algısal benzerliği 0–1 arası bir skala ile ölçülür.  
> Bu projede elde edilen ortalama LPIPS skoru **0.5386** olup, bu değer Pixar tarzı yüksek stilizasyon içeren dönüşümlerde kabul edilebilir düzeydedir.

###  SSIM Kalite Değerlendirme (Yapısal Benzerlik)

| Görsel         | SSIM Skoru |
|----------------|-------------|
| `input1.jpg`   | 0.4399      |
| `input2.jpg`   | 0.3618      |
| **Ortalama**   | **0.4008**  |

> Görsel kaliteyi yapısal yönden değerlendirmek için **SSIM (Structural Similarity Index)** metriği kullanılmıştır.  
> Bu metrik, renk ve doku gibi detaylar yerine yapının, kenarların ve kontrastın korunma düzeyini ölçer.  
> 0.4008'lik ortalama skor, yoğun stilizasyon uygulanan bu projede yapısal bozulmanın kabul edilebilir düzeyde olduğunu göstermektedir.

---

## Proje İşlevselliği

**Video ve Görsel Dönüştürme**: Gerçek video ve görselleri karelere ayırarak Pixar tarzı animasyona dönüştürür.  
**Yapay Zeka Destekli Stilizasyon**: ToonYou, LoRA ile Pixar modelleri kullanılarak stil değişimi uygular.  
**Pixar Tarzı Görselleştirme**: 3D çizgi film estetiğine yakın sonuçlar üretir.  
**Kalite Ölçümleme**: LPIPS ve SSIM metrikleri ile görsel kalite bilimsel olarak analiz edilir.  
**Tam Yerel Sistem**: API’siz, tamamen yerel çalışır. İnternete ihtiyaç duymaz.

---

##  Geliştirici

Bu proje **Burak AVCI** tarafından geliştirilmiştir.  
 burakavci0206@gmail.com

---

##  Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyaç vardır:

- Python 3.10.11  
- NVIDIA GPU + CUDA desteği  
- Gerekli Python kütüphaneleri:

```bash
pip install torch
pip install torchvision
pip install lpips
pip install opencv-python
pip install tqdm
pip install pandas
pip install scikit-image
