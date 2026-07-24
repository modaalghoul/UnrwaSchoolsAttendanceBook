"""Styling for the Attendance Book Generator application"""

# Main window stylesheet
MAIN_WINDOW_STYLE = """
QMainWindow {
    background-color: #f5f5f5;
}

QLabel {
    color: #333333;
}

QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #45a049;
}

QPushButton:pressed {
    background-color: #3d8b40;
}

QPushButton:disabled {
    background-color: #cccccc;
    color: #666666;
}

QGroupBox {
    font-weight: bold;
    border: 2px solid #4CAF50;
    border-radius: 6px;
    margin-top: 12px;
    padding-top: 10px;
    background-color: white;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 10px;
    color: #4CAF50;
}

QRadioButton {
    spacing: 8px;
    color: #333333;
}

QRadioButton::indicator {
    width: 18px;
    height: 18px;
}

QRadioButton::indicator:unchecked {
    border: 2px solid #999999;
    border-radius: 9px;
    background-color: white;
}

QRadioButton::indicator:checked {
    border: 2px solid #4CAF50;
    border-radius: 9px;
    background-color: #4CAF50;
}

QCheckBox {
    spacing: 8px;
    color: #333333;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
}

QCheckBox::indicator:unchecked {
    border: 2px solid #999999;
    border-radius: 3px;
    background-color: white;
}

QCheckBox::indicator:checked {
    border: 2px solid #4CAF50;
    border-radius: 3px;
    background-color: #4CAF50;
    image: url(none);
}

QComboBox {
    border: 2px solid #cccccc;
    border-radius: 4px;
    padding: 4px 8px;
    background-color: white;
    min-width: 100px;
}

QComboBox:hover {
    border: 2px solid #4CAF50;
}

QComboBox::drop-down {
    border: none;
}

QDateEdit, QSpinBox {
    border: 2px solid #cccccc;
    border-radius: 4px;
    padding: 4px 8px;
    background-color: white;
}

QDateEdit:hover, QSpinBox:hover {
    border: 2px solid #4CAF50;
}

QProgressBar {
    border: 2px solid #4CAF50;
    border-radius: 5px;
    text-align: center;
    background-color: white;
}

QProgressBar::chunk {
    background-color: #4CAF50;
    border-radius: 3px;
}
"""

# Title label style
TITLE_STYLE = """
QLabel {
    color: #2c3e50;
    background-color: white;
    padding: 15px;
    border-radius: 8px;
    border: 2px solid #4CAF50;
}
"""

# Status label style
STATUS_STYLE = """
QLabel {
    color: #555555;
    padding: 5px;
    background-color: #e8f5e9;
    border-radius: 4px;
}
"""

# File label style
FILE_LABEL_STYLE = """
QLabel {
    color: #666666;
    padding: 5px;
    background-color: #f9f9f9;
    border: 1px solid #dddddd;
    border-radius: 3px;
}
"""

# Create button style
CREATE_BUTTON_STYLE = """
QPushButton {
    background-color: #2196F3;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    font-weight: bold;
    font-size: 12pt;
}

QPushButton:hover {
    background-color: #1976D2;
}

QPushButton:pressed {
    background-color: #0D47A1;
}

QPushButton:disabled {
    background-color: #cccccc;
    color: #666666;
}
"""

# Instructions label style
INSTRUCTIONS_STYLE = """
QLabel {
    color: #555555;
    padding: 8px;
    background-color: #fff3cd;
    border-radius: 4px;
    border: 1px solid #ffc107;
}
"""

# Credit label style
CREDIT_STYLE = """
QLabel {
    color: #888888;
    padding: 10px;
    background-color: transparent;
    font-style: italic;
}
"""
