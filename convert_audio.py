import os
import tkinter as tk
from tkinter import filedialog
from moviepy import AudioFileClip

def convert_and_cleanup():
    root = tk.Tk()
    root.withdraw() # Hide the main window

    print("--- Converter & Cleanup Started ---")
    print("⚠️ WARNING: This will DELETE the original files after conversion.")
    print("👉 Please select the FOLDER containing your songs...")
    
    # 1. Open FOLDER selector
    folder_path = filedialog.askdirectory(
        title="Select Folder (Originals will be DELETED after conversion)"
    )

    if not folder_path:
        print("❌ No folder selected. Exiting.")
        return

    print(f"📂 Scanning folder: {folder_path}\n")
    
    # 2. Find files (excluding .mp3)
    supported_extensions = (".mp4", ".m4a", ".wav", ".mkv", ".mov")
    files_to_convert = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_extensions)]

    if not files_to_convert:
        print("❌ No files found to convert (or only MP3s exist).")
        return

    print(f"Found {len(files_to_convert)} files. Starting process...\n")

    # 3. Loop, Convert, Delete
    count = 0
    for filename in files_to_convert:
        count += 1
        file_path = os.path.join(folder_path, filename)
        
        # New MP3 filename
        base_name = os.path.splitext(filename)[0]
        mp3_path = os.path.join(folder_path, base_name + ".mp3")

        print(f"[{count}/{len(files_to_convert)}] 🔄 Processing: {filename}...")

        try:
            # Conversion
            clip = AudioFileClip(file_path)
            clip.write_audiofile(mp3_path, bitrate="192k", logger=None)
            clip.close() # Important: Release file so it can be deleted
            
            # Deletion
            os.remove(file_path) 
            print(f"   ✅ Converted & Deleted original file.")
            
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            print("   (Original file was NOT deleted due to error)")

    print("\n🎉 All done! Only MP3 files remain.")

if __name__ == "__main__":
    convert_and_cleanup()