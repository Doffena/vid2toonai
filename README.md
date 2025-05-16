## 🎬 Pixar Görsel Karşılaştırmaları

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

## 🎥 Örnek Videolar

- [📹 Video 1](example_outputs/result1.mp4)  
- [📹 Video 2](example_outputs/result2.mp4)

### 📊 LPIPS Kalite Değerlendirme

| Görsel         | LPIPS Skoru |
|----------------|--------------|
| `input1.jpg`   | 0.4892       |
| `input2.jpg`   | 0.5880       |
| **Ortalama**   | **0.5386**   |

> Görsel kalitenin değerlendirilmesi için **LPIPS (Learned Perceptual Image Patch Similarity)** metriği kullanılmıştır.  
> Stilize edilen görsellerin orijinallerine algısal benzerliği 0–1 arası bir skala ile ölçülür.  
> Bu projede elde edilen ortalama LPIPS skoru **0.5386** olup, bu değer Pixar tarzı yüksek stilizasyon içeren dönüşümlerde kabul edilebilir düzeydedir.

### 📊 SSIM Kalite Değerlendirme (Yapısal Benzerlik)

| Görsel         | SSIM Skoru |
|----------------|-------------|
| `input1.jpg`   | 0.4399      |
| `input2.jpg`   | 0.3618      |
| **Ortalama**   | **0.4008**  |

> Görsel kaliteyi yapısal yönden değerlendirmek için **SSIM (Structural Similarity Index)** metriği kullanılmıştır.  
> Bu metrik, renk ve doku gibi detaylar yerine yapının, kenarların ve kontrastın korunma düzeyini ölçer.  
> 0.4008'lik ortalama skor, yoğun stilizasyon uygulanan bu projede yapısal bozulmanın kabul edilebilir düzeyde olduğunu göstermektedir.
