"""
Attendance Book Generator - Main Entry Point
A PyQt6 application for generating student attendance books
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

from ui.main_window import AttendanceApp


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set Arabic font
    font = QFont("Arial", 10)
    app.setFont(font)
    
    # Create and show main window
    window = AttendanceApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()