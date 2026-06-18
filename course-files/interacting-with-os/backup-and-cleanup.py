import shutil
from pathlib import Path

def create_backup(source_dir: str | Path, dest_dir: str | Path) -> None:
    """
    Creates a clean backup of a source directory to a destination directory.

    If the destination directory exists, it is removed before copying.

    Args:
        source_dir (Union[str, Path]): The directory to back up.
        dest_dir (Union[str, Path]): The directory to create the backup in.
    """
    # TODO: Implement input validation.

    for arg in [source_dir, dest_dir]:
        if not isinstance(arg, (str, Path)):
            raise TypeError(f"Arguments must be of type String or pathlib.Path: {arg}")

    source_dir = Path(source_dir)

    if not source_dir.is_dir() or not source_dir.exists():
        raise ValueError("directory didn't exists")
    
    # TODO: Check if the destination exists; if yes, remove it.

    dest_dir = Path(dest_dir)

    if dest_dir.exists():
        shutil.rmtree(dest_dir)

    # TODO: Copy the source to the destination.

    shutil.copytree(source_dir, dest_dir)
