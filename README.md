# OpenCV Temel G�r�nt� ��leme Uygulamalar�

Python ile k��e ve kenar tespiti, g�r�lt� azaltma, kamera kullan�m� ve Haar cascade uygulamalar�.

## Temel OpenCV uygulamalar�

| Dosya | ��lev | Girdi |
|---|---|---|
| `corner_detection.py` | Harris, Shi-Tomasi ve Canny kar��la�t�rmas� | `cat_image.jpg`, `sudoku.jpg` |
| `denoise.py` | Bilateral filtre ile g�r�lt� azaltma | `image3.jpeg` |
| `face_detection.py` | Haar cascade ile kamerada y�z, g�z ve g�l�mseme tespiti | Kamera 0, `cascade/` |
| `oppening_Cam.py` | Kameradan gri tonlamal� g�r�nt� | Kamera 0 |
| `rgb_output.py` | T�klanan video pikselinin RGB de�erlerini yazd�rma | Kullan�c�n�n sa�layaca�� `video.mp4` |

## Kurulum ve kullan�m

Python 3.10 veya �zeri bir sanal ortam �nerilir. Ba��ml�l�k s�r�mleri sabitlenmemi�tir; bu depo do�rulanm�� bir ortam kilidi i�ermez.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python corner_detection.py
python face_detection.py --cascade cascade
```

Bu komutlar� depo k�k�nden �al��t�r�n. Kamera ve video pencerelerinde `q` ile ��k�l�r. OpenCV pencereleri i�in masa�st� oturumu gerekir.


video.mp4 depoya dahil de�ildir; rgb_output.py i�in kendi videonuzu bu adla depo k�k�ne koyun. Cascade XML dosyalar�ndaki ���nc� taraf lisans bildirimleri korunmu�tur.
