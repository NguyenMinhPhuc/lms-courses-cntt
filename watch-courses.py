import time
import sys
from pathlib import Path
import subprocess

# Fix Windows console encoding
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = Path(__file__).resolve().parent

def get_current_folders():
    return sorted([
        f.name for f in ROOT_DIR.iterdir()
        if f.is_dir() and not f.name.startswith(".") and (f / "index.html").is_file()
    ])

def main():
    print("=" * 60)
    print("LMS COURSES CNTT - REAL-TIME FOLDER WATCHER")
    print(f"Monitoring: {ROOT_DIR}")
    print("Whenever you add/remove a course folder with index.html,")
    print("this watcher will automatically update courses.json & courses-data.js.")
    print("=" * 60)

    last_folders = get_current_folders()
    print(f"Initial courses detected ({len(last_folders)}): {', '.join(last_folders)}")
    
    # Run scan once at start
    subprocess.run([sys.executable, str(ROOT_DIR / "scan-courses.py")], check=False)

    try:
        while True:
            time.sleep(2)
            current_folders = get_current_folders()
            if current_folders != last_folders:
                print(f"\n[Change Detected!] New folder list: {current_folders}")
                subprocess.run([sys.executable, str(ROOT_DIR / "scan-courses.py")], check=False)
                last_folders = current_folders
    except KeyboardInterrupt:
        print("\nWatcher stopped.")

if __name__ == "__main__":
    main()

