"""Constants and configurations for the Attendance Book Generator"""

# Arabic month names
MONTH_NAMES_ARABIC = [
    "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
    "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"
]

# Arabic day names
DAY_NAMES_ARABIC = ['أحد', 'اثنين', 'ثلاثاء', 'أربعاء', 'خميس', 'جمعة', 'سبت']

# Daily attendance headers
DAILY_HEADERS = ['الرقم', 'الاسم', 'حضور', 'غياب', 'التوقيع', 'ملاحظات']

# Column widths for daily sheet
DAILY_COLUMN_WIDTHS = {
    'A': 8,   # الرقم
    'B': 25,  # الاسم
    'C': 8,   # حضور
    'D': 8,   # غياب
    'E': 12,  # التوقيع
    'F': 15   # ملاحظات
}

# Column widths for monthly sheet
MONTHLY_COLUMN_WIDTHS = {
    'number': 6,   # الرقم
    'name': 28,    # الاسم
    'day': 4,      # الأيام
    'total': 8     # المجموع
}

# Font sizes
FONT_SIZES = {
    'header': 16,
    'day_name': 10,
    'name': 12,
    'title': 16
}

# Maximum number of names to extract
MAX_NAMES = 50

# Year range for date selection
YEAR_RANGE = (2020, 2030)
