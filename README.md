# Attendance Book Generator

A PyQt6 desktop application for generating student attendance books from Excel files, tailored for UNRWA schools in Jordan.

## English

### Features
- Daily and monthly attendance reports
- Support for Jordan public holidays
- Arabic-friendly RTL interface
- Ready-to-print Excel output for UNRWA school use

### Installation
1. Open the project folder in a terminal.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   ```bash
   .\.venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python main.py
   ```

### Build executable
```bash
python build.py
```

### Project Structure
```text
main.py
core/
ui/
utils/
```

### Requirements
- PyQt6
- xlrd
- openpyxl
- holidays
- pyinstaller

---

## العربية

# مولد دفتر الغياب

تطبيق سطح مكتبي باستخدام PyQt6 لإنشاء دفاتر غياب للطلاب من ملفات Excel، مصمم خصيصًا لمدارس الأونروا في الأردن.

### الميزات
- تقارير يومية وشهرية
- دعم العطل الرسمية في الأردن
- واجهة عربية وداعمة لاتجاه اليمين إلى اليسار
- إنشاء ملفات Excel جاهزة للطباعة لاستخدام مدارس الأونروا

### التثبيت
1. افتح المجلد في سطر الأوامر.
2. أنشئ بيئة افتراضية:
   ```bash
   python -m venv .venv
   ```
3. شغّل البيئة:
   ```bash
   .\.venv\Scripts\activate
   ```
4. ثبّت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```
5. شغّل التطبيق:
   ```bash
   python main.py
   ```

### البناء إلى ملف قابل للتنفيذ
```bash
python build.py
```

