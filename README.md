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

📊 LPIPS Kalite Değerlendirme
Görsel	LPIPS Skoru
input1.jpg	0.4892
input2.jpg	0.5880
Ortalama	0.5386

Görsel kalitenin değerlendirilmesi için LPIPS (Learned Perceptual Image Patch Similarity) metriği kullanılmıştır.
Stilize edilen görsellerin orijinallerine algısal benzerliği 0–1 arası bir skala ile ölçülür.
Bu projede elde edilen ortalama LPIPS skoru 0.5386 olup, bu değer Pixar tarzı yüksek stilizasyon içeren dönüşümlerde kabul edilebilir düzeydedir.