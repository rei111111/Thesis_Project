from pathlib import Path


def add_txt_extensions(folder: Path) -> int:
    """Rename extensionless collection files only when explicitly invoked."""
    if not folder.is_dir():
        raise FileNotFoundError(f"Collection directory does not exist: {folder}")
    renamed = 0
    for path in folder.iterdir():
        if path.is_file() and path.suffix == "":
            path.rename(path.with_suffix(".txt"))
            renamed += 1
    return renamed


if __name__ == "__main__":
    collection_directory = Path(__file__).resolve().parent / "Videos"
    print(f"Renamed {add_txt_extensions(collection_directory)} files.")
