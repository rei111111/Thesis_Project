from pathlib import Path

# Path to the existing Videos folder
videos_dir = Path("YT_Shorts_wm222dk_transcription\Videos")  # Or Path("../Videos"), etc., depending on its location

# Create files: video6 to video250
for i in range(6, 251):
    file_path = videos_dir / f"video{i}"
    file_path.touch(exist_ok=True)

print("Files created successfully.")