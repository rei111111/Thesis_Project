from pathlib import Path

folder = Path("YT_Shorts_wm222dk_transcription\Videos")

for file in folder.iterdir():
    if file.is_file() and file.suffix == "":
        file.rename(file.with_suffix(".txt"))