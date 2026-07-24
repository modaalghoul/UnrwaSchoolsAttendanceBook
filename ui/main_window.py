"""Main window UI for the Attendance Book Generator"""

import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QLabel, QFileDialog, QComboBox, QMessageBox, QProgressBar,
    QGroupBox, QRadioButton, QDateEdit, QSpinBox, QCheckBox
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

from core.processor import AttendanceProcessor
from ui.styles import (
    MAIN_WINDOW_STYLE, TITLE_STYLE, STATUS_STYLE,
    FILE_LABEL_STYLE, CREATE_BUTTON_STYLE
)
from utils.constants import MONTH_NAMES_ARABIC, YEAR_RANGE


class AttendanceApp(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.input_file = ""
        self.output_file = ""
        self.setup_ui()
        self.apply_styles()
        
    def setup_ui(self):
        """Setup the user interface"""
        self.setWindowTitle("تطبيق دفتر غياب الطلاب")
        self.setGeometry(300, 300, 650, 550)
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        self.title_label = QLabel("تطبيق إنشاء دفتر غياب الطلاب")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        layout.addWidget(self.title_label)
        
        # Instructions
        self.instructions_label = QLabel('قم بتحميل تقرير "كشف اسماء الطلاب" من الايميس')
        self.instructions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instructions_font = QFont()
        instructions_font.setPointSize(10)
        self.instructions_label.setFont(instructions_font)
        layout.addWidget(self.instructions_label)
        
        # Files section
        self._create_files_section(layout)
        
        # Report type section
        self._create_report_section(layout)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMinimumHeight(25)
        layout.addWidget(self.progress_bar)
        
        # Status label
        self.status_label = QLabel("جاهز للاستخدام")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Create button
        self.create_btn = QPushButton("إنشاء دفتر الغياب")
        self.create_btn.clicked.connect(self.create_attendance_book)
        self.create_btn.setMinimumHeight(50)
        create_font = QFont()
        create_font.setPointSize(12)
        create_font.setBold(True)
        self.create_btn.setFont(create_font)
        layout.addWidget(self.create_btn)
        
        layout.addStretch()
        
        # Developer credit
        self.credit_label = QLabel("Developed with ❤️ by Mohammad Alghoul\nJofeh Prep Boys School")
        self.credit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credit_font = QFont()
        credit_font.setPointSize(8)
        self.credit_label.setFont(credit_font)
        layout.addWidget(self.credit_label)
        
    def _create_files_section(self, layout):
        """Create the files selection section"""
        files_group = QGroupBox("إعدادات الملفات")
        files_layout = QVBoxLayout(files_group)
        files_layout.setSpacing(10)
        
        # Input file
        input_layout = QHBoxLayout()
        self.input_label = QLabel("لم يتم اختيار ملف")
        self.input_btn = QPushButton("اختيار ملف Excel للطلاب")
        self.input_btn.clicked.connect(self.select_input_file)
        input_layout.addWidget(self.input_btn)
        input_layout.addWidget(self.input_label, 1)
        files_layout.addLayout(input_layout)
        
        # Output file
        output_layout = QHBoxLayout()
        self.output_label = QLabel("لم يتم تحديد مسار الحفظ")
        self.output_btn = QPushButton("اختيار مسار حفظ دفتر الغياب")
        self.output_btn.clicked.connect(self.select_output_file)
        output_layout.addWidget(self.output_btn)
        output_layout.addWidget(self.output_label, 1)
        files_layout.addLayout(output_layout)
        
        layout.addWidget(files_group)
    
    def _create_report_section(self, layout):
        """Create the report type section"""
        report_group = QGroupBox("نوع التقرير")
        report_layout = QVBoxLayout(report_group)
        report_layout.setSpacing(10)
        
        # Report type radio buttons
        radio_layout = QHBoxLayout()
        self.daily_radio = QRadioButton("تقرير يومي")
        self.monthly_radio = QRadioButton("تقرير شهري")
        self.daily_radio.setChecked(True)
        self.daily_radio.toggled.connect(self.on_report_type_changed)
        radio_layout.addWidget(self.daily_radio)
        radio_layout.addWidget(self.monthly_radio)
        radio_layout.addStretch()
        report_layout.addLayout(radio_layout)
        
        # Date settings
        date_layout = QHBoxLayout()
        
        # Daily report date
        self.date_label = QLabel("التاريخ:")
        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        
        # Monthly report date
        self.month_label = QLabel("الشهر:")
        self.month_combo = QComboBox()
        self.month_combo.addItems(MONTH_NAMES_ARABIC)
        self.month_combo.setCurrentIndex(datetime.now().month - 1)
        
        self.year_label = QLabel("السنة:")
        self.year_spin = QSpinBox()
        self.year_spin.setRange(*YEAR_RANGE)
        self.year_spin.setValue(datetime.now().year)
        
        date_layout.addWidget(self.date_label)
        date_layout.addWidget(self.date_edit)
        date_layout.addWidget(self.month_label)
        date_layout.addWidget(self.month_combo)
        date_layout.addWidget(self.year_label)
        date_layout.addWidget(self.year_spin)
        date_layout.addStretch()
        
        report_layout.addLayout(date_layout)
        
        # Holiday highlighting option
        self.highlight_holidays_check = QCheckBox(
            "تمييز أيام الجمعة والسبت والعطل الرسمية بلون رمادي"
        )
        self.highlight_holidays_check.setChecked(True)
        report_layout.addWidget(self.highlight_holidays_check)
        
        layout.addWidget(report_group)
        
        # Update date controls visibility
        self.on_report_type_changed()
    
    def apply_styles(self):
        """Apply stylesheets to the window"""
        from ui.styles import INSTRUCTIONS_STYLE, CREDIT_STYLE
        
        self.setStyleSheet(MAIN_WINDOW_STYLE)
        self.title_label.setStyleSheet(TITLE_STYLE)
        self.instructions_label.setStyleSheet(INSTRUCTIONS_STYLE)
        self.status_label.setStyleSheet(STATUS_STYLE)
        self.input_label.setStyleSheet(FILE_LABEL_STYLE)
        self.output_label.setStyleSheet(FILE_LABEL_STYLE)
        self.create_btn.setStyleSheet(CREATE_BUTTON_STYLE)
        self.credit_label.setStyleSheet(CREDIT_STYLE)
    
    def on_report_type_changed(self):
        """Update date controls based on report type"""
        is_daily = self.daily_radio.isChecked()
        
        self.date_label.setVisible(is_daily)
        self.date_edit.setVisible(is_daily)
        self.month_label.setVisible(not is_daily)
        self.month_combo.setVisible(not is_daily)
        self.year_label.setVisible(not is_daily)
        self.year_spin.setVisible(not is_daily)
    
    def select_input_file(self):
        """Select input Excel file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "اختيار ملف Excel للطلاب",
            "",
            "Excel Files (*.xls *.xlsx)"
        )
        if file_path:
            self.input_file = file_path
            self.input_label.setText(os.path.basename(file_path))
    
    def select_output_file(self):
        """Select output file path"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "حفظ دفتر الغياب",
            "دفتر_الغياب.xlsx",
            "Excel Files (*.xlsx)"
        )
        if file_path:
            self.output_file = file_path
            self.output_label.setText(os.path.basename(file_path))
    
    def create_attendance_book(self):
        """Start attendance book creation process"""
        if not self.input_file:
            QMessageBox.warning(self, "تحذير", "يرجى اختيار ملف Excel للطلاب")
            return
        
        if not self.output_file:
            QMessageBox.warning(self, "تحذير", "يرجى تحديد مسار حفظ دفتر الغياب")
            return
        
        # Determine report type and date info
        report_type = "daily" if self.daily_radio.isChecked() else "monthly"
        highlight_holidays = self.highlight_holidays_check.isChecked()
        
        if report_type == "daily":
            date_info = self.date_edit.date()
        else:
            date_info = {
                'year': self.year_spin.value(),
                'month': self.month_combo.currentIndex() + 1
            }
        
        # Start processing
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.create_btn.setEnabled(False)
        
        self.processor = AttendanceProcessor(
            self.input_file,
            self.output_file,
            report_type,
            date_info,
            highlight_holidays
        )
        self.processor.progress_updated.connect(self.progress_bar.setValue)
        self.processor.status_updated.connect(self.status_label.setText)
        self.processor.finished.connect(self.on_processing_finished)
        self.processor.error_occurred.connect(self.on_processing_error)
        self.processor.start()
    
    def on_processing_finished(self, message):
        """Handle successful processing completion"""
        self.progress_bar.setVisible(False)
        self.create_btn.setEnabled(True)
        self.status_label.setText("جاهز للاستخدام")
        QMessageBox.information(self, "نجح", message)
    
    def on_processing_error(self, error_message):
        """Handle processing error"""
        self.progress_bar.setVisible(False)
        self.create_btn.setEnabled(True)
        self.status_label.setText("حدث خطأ")
        QMessageBox.critical(self, "خطأ", error_message)
