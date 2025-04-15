محول الفيديو إلى GIF - Video to GIF Converter
=================================

تثبيت التطبيق على نظام ويندوز Windows:
عند تثبيت مكتبات Qt5 على نظام Windows، الطريقة تختلف عن Linux. في Windows، يمكنك اتباع الخطوات التالية:
قم بتحميل Qt Online Installer من الموقع الرسمي:
اذهب إلى https://www.qt.io/download-qt-installer
قم بتحميل Qt Online Installer لنظام Windows
عند تشغيل المثبت:
اختر "Custom Installation"
في قائمة المكونات، تأكد من اختيار:
Qt > Qt 5.15.x (أو أحدث إصدار Qt5)
توجه إلى المكونات التالية وقم بتحديدها:
MSVC (إذا كنت تستخدم Visual Studio)
MinGW
Qt WebEngine
Developer and Designer Tools
بعد التثبيت، تأكد من إضافة مسار Qt bin إلى متغيرات النظام (System PATH):
المسار النموذجي سيكون مثل: C:\Qt\5.15.x\mingw81_64\bin C:\Qt\Tools\mingw810_64\bin
ملاحظة: يمكنك أيضاً استخدام مدير الحزم Chocolatey إذا كان مثبتاً على جهازك، باستخدام الأمر:
choco install qt5-sdk
1. تأكد من وجود ملف videotogif-setup.exe في هذا المجلد
2. انقر نقراً مزدوجاً على الملف
3. اتبع خطوات المعالج للتثبيت

بعد التثبيت:
- ستجد التطبيق في قائمة Start
- سيتم إنشاء اختصار على سطح المكتب

إلغاء التثبيت:
1. من لوحة التحكم Control Panel:
   - افتح "البرامج والميزات" Programs and Features
   - ابحث عن "Video to GIF"
   - اضغط على زر "إلغاء التثبيت"
2. أو من قائمة Start:
   - اضغط بالزر الأيمن على التطبيق
   - اختر "إلغاء التثبيت"

المتطلبات:
- سيتم تثبيتها تلقائياً (FFmpeg, Qt5)

--------------------
معلومات المطور:
--------------------
الاسم: linuxlaghouat

تابعونا على:
-----------
فيسبوك: https://www.facebook.com/LinuxLaghouatAlgeria
يوتيوب: https://www.youtube.com/@linuxlaghouat
المدونة: https://linuxlaghouat.blogspot.com/
تويتر: https://x.com/linuxlaghouat

© 2025 Linux Laghouat. جميع الحقوق محفوظة.
