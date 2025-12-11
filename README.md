# 🎵 Audio Files Conversion Script

A simple and efficient Python tool to batch convert audio/video files (MP4, M4A, WAV, etc.) to **MP3 format**.

It includes features to select entire folders via a graphical popup window and optionally delete the original files to clean up your library.

## ✨ Features

* **Batch Conversion:** Convert an entire folder of songs at once.
* **Wide Format Support:** Handles `.mp4`, `.m4a`, `.wav`, `.mov`, `.mkv` files.
* **Auto-Cleanup:** Automatically deletes the original source file after a successful conversion (saves disk space).
* **User Friendly:** Uses a popup window to select folders—no complex command line paths required.
* **High Quality:** Converts audio to 192k bitrate MP3s.

## 🚀 Installation

### 1. Install Python
Make sure you have Python installed on your system. [Download Python Here](https://www.python.org/downloads/)

### 2. Install Dependencies
Open your terminal (Command Prompt or PowerShell) and run:

pip install moviepy
Note: This script uses moviepy, which is compatible with Python 3.13+ (unlike older pydub scripts).

🛠️ How to Use
Download the script (convert_audio.py) to your computer.

Run the script:

python convert_audio.py
Select your Folder: A window will pop up. Navigate to the folder containing your music/video files and select it.

Watch it work: The script will loop through every file, convert it to MP3, and remove the old file.

⚠️ Important Warning
This script acts as a converter & cleaner. It will PERMANENTLY DELETE the original source files (e.g., M4A, MP4) after creating the MP3 version.

If you want to keep the originals: Modify the script to remove the os.remove(file_path) line.

📝 Requirements
Python 3.x

moviepy library

tkinter (usually comes pre-installed with Python)
