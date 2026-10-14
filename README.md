# OpenCV Temel Görüntü İşleme Uygulamaları

Python ile köşe ve kenar tespiti, gürültü azaltma, kamera kullanımı ve Haar cascade uygulamaları.

## Temel OpenCV uygulamaları

| Dosya | İşlev | Girdi |
|---|---|---|
| `corner_detection.py` | Harris, Shi–Tomasi ve Canny karşılaştırması | `cat_image.jpg`, `sudoku.jpg` |
| `denoise.py` | Bilateral filtre ile gürültü azaltma | `image3.jpeg` |
| `face_detection.py` | Haar cascade ile kamerada yüz, göz ve gülümseme tespiti | Kamera 0, `cascade/` |
| `oppening_Cam.py` | Kameradan gri tonlamalı görüntü | Kamera 0 |
| `rgb_output.py` | Tıklanan video pikselinin RGB değerlerini yazdırma | Kullanıcının sağlayacağı `video.mp4` |

## Kurulum ve kullanım

Python 3.10 veya üzeri bir sanal ortam önerilir. Bağımlılık sürümleri sabitlenmemiştir; bu depo doğrulanmış bir ortam kilidi içermez.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python corner_detection.py
python face_detection.py --cascade cascade
```

Bu komutları depo kökünden çalıştırın. Kamera ve video pencerelerinde `q` ile çıkılır. OpenCV pencereleri için masaüstü oturumu gerekir.


video.mp4 depoya dahil değildir; rgb_output.py için kendi videonuzu bu adla depo köküne koyun. Cascade XML dosyalarındaki üçüncü taraf lisans bildirimleri korunmuştur.
