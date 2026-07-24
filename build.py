import PyInstaller.__main__
import os
APP_NAME = "Attendance Book Generator"


def build_executables():
    # Build main application
    PyInstaller.__main__.run([
        'main.py',
        '--name=' + APP_NAME,
        '--onefile',
        '--console',
        '--icon=iconpng.png',
        '--hidden-import=holidays',
        '--hidden-import=holidays.countries',

    ])

if __name__ == "__main__":
    build_executables() 