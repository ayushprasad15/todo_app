import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compress.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["bonus8.py", "bonus3.py"], dest_dir="dest3.py")
