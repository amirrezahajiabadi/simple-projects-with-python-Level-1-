from pathlib import Path
import shutil

base_dir = Path(r"D:\photo\UNI")
target_dir = base_dir / "sorted"

FILE_CATEGORIES = {
    "images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "videos":    [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio":     [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives":  [".zip", ".rar", ".tar", ".gz", ".7z"],
    "others":    []  
}

def create_category_directories():
    for category in FILE_CATEGORIES:
        (target_dir / category).mkdir(parents=True, exist_ok=True)

def get_category(suffix: str) -> str:
    suffix = suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if suffix in extensions:
            return category
    return "others"

def search_and_categorize_files():
    copied, skipped = 0, 0

    for file in base_dir.rglob("*"):
        if target_dir in file.parents:
            continue

        if not file.is_file():
            continue

        category = get_category(file.suffix)
        dest = target_dir / category / file.name

        
        if dest.exists():
            print(f"[SKIP] {file.name}")
            skipped += 1
            continue

        try:
            shutil.copy2(file, dest)
            print(f"[OK] {file.name}  →  {category}/")
            copied += 1
        except Exception as e:
            print(f"[ERROR] {file.name}: {e}")

    print(f"\n✅ {copied}| ⏭ {skipped} ")

create_category_directories()
search_and_categorize_files()