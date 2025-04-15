# محول الفيديو إلى GIF - نسخة الويب

تطبيق ويب لتحويل الفيديو إلى صور متحركة GIF باستخدام Flask و Python.

## المتطلبات

- Python 3.8+
- FFmpeg

## التثبيت

1. قم بإنشاء بيئة Python افتراضية:
```bash
python -m venv venv
source venv/bin/activate  # على Linux/macOS
# أو
venv\Scripts\activate  # على Windows
```

2. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

3. تأكد من تثبيت FFmpeg على نظامك:
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: قم بتحميله من [الموقع الرسمي](https://ffmpeg.org/download.html)

## التشغيل

1. تشغيل التطبيق في وضع التطوير:
```bash
flask run
```

2. تشغيل التطبيق في وضع الإنتاج:
```bash
gunicorn app:app
```

يمكنك الوصول إلى التطبيق على: http://localhost:5000

## الميزات

- تحويل الفيديو إلى GIF
- التحكم في:
  - وقت البداية والنهاية
  - حجم الصورة الناتجة
  - سرعة العرض (FPS)
- دعم ملفات فيديو متعددة (mp4, avi, mov, mkv)
- حد أقصى لحجم الملف: 200 ميجابايت
- معاينة مباشرة للصورة المتحركة
- واجهة مستخدم سهلة الاستخدام
- Linux : https://mega.nz/file/RGEVkCDY#fR67vTQjqUB-rdftBXRKyH6if8fCSgNfbfOfpwKKiEU
- Windows : https://mega.nz/file/NX8gFApJ#JZLWa955iuHMtwKdWZKzfPRbT0M1uZ-OU4KLXlaG2sc


## معلومات المطور

- الاسم: Linux Laghouat
- المدونة: [linuxlaghouat.blogspot.com](https://linuxlaghouat.blogspot.com/)
- فيسبوك: [LinuxLaghouatAlgeria](https://www.facebook.com/LinuxLaghouatAlgeria)
- يوتيوب: [@linuxlaghouat](https://www.youtube.com/@linuxlaghouat)
- تويتر: [@linuxlaghouat](https://x.com/linuxlaghouat)

© 2025 Linux Laghouat. جميع الحقوق محفوظة.
