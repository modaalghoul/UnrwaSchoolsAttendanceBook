# Attendance Book Generator

A PyQt6 desktop application for generating student attendance books from Excel files.

English | [العربية](README_AR.md)

## Features
- Daily and monthly attendance reports
- Support for Jordan public holidays
- Arabic-friendly RTL interface
- Ready-to-print Excel output

## Installation
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

## Build executable
```bash
python build.py
```

## Project Structure
```text
main.py
core/
ui/
utils/
```

## Requirements
- PyQt6
- xlrd
- openpyxl
- holidays
- pyinstaller

