# Runs with pwsh
#exec(open("main.py").read())
import os
import pathlib
import shutil
import stat # To interpret results of os.stat()
from datetime import datetime as dt
if __name__ == "__main__":
    file_path = ".\\resources"

    # Get full path of a directory
    dir_path = os.path.abspath(".")
    print(f"Full path of this directory: {dir_path}", end = "\n")

    # Append to a path
    file_name = os.path.join(file_path, "plaintext.txt")
    print(f"file_name = {file_name}")

    # Read file contents as text
    fl = open(file_name, "rt")
    contents = fl.read()
    print("----------------------------------------")
    print(f"  Contents of {file_name}")
    print("----------------------------------------")
    print(contents, end = "\n\n\n")
    fl.close()

    # Write text t file
    some_str = "some trivial content"
    # with closes file after block ends
    with open(os.path.join(file_path, "deleteme.txt"), "wt") as fl:
        fl.write(some_str)

    # Get a list of all files in a directory using os.listdir()
    # os.listdir() is for legacy versions
    dirs = []
    files = []
    for p in os.listdir(dir_path):
        # Full path of file
        full_path = os.path.join(dir_path, p)

        # Append to different lists depending on whether or not the target is a
        # file or directory
        if os.path.isfile(full_path):
            files.append(full_path)
        if os.path.isdir(full_path):
            dirs.append(full_path)

    # Get a list of all files in a directory using os.scandir()
    # os.scandir() returns an Iterator[nt.DirEntry]
    dirs.clear()
    files.clear()
    for dir_entry in os.scandir(dir_path):
        if dir_entry.is_dir():
            dirs.append(dir_entry.path)
        if dir_entry.is_file():
            files.append(dir_entry.path)
        # print(f"    name: {dir_entry.name}")
        # print(f"    path: {dir_entry.path}")
        # print(f"    inode(): {dir_entry.inode()}")
        # print(f"    is_dir(): {dir_entry.is_dir()}")
        # print(f"    is_file(): {dir_entry.is_file()}")
        # print(f"    is_symlink(): {dir_entry.is_symlink()}")
        # print(f"    stat(): {dir_entry.stat()}")

    # Get a list of all files in d adirectory using pathlib
    # pathlib.Path().iterdir() returns a generator whose elements are either
    # PosixPath or WindowsPath
    dirs.clear()
    files.clear()
    for p in pathlib.Path("..").iterdir():
        # See documentation for PurePath/Path for methods and properties.
        if p.is_dir():
            dirs.append(p)
        if p.is_file():
            files.append(p)

    # Get file attributes
    info = os.stat(os.path.join(dir_path, "main.py"))
    mode = info.st_mode
    print(f"S_ISDIR = {stat.S_ISDIR(mode)}")                # file is a directory
    print(f"S_ISREG = {stat.S_ISREG(mode)}")                # file is a regular file
    print(f"ST_SIZE = {info.st_size}")                      # size of the file in bytes
    print(f"ST_ATIME = {dt.fromtimestamp(info.st_atime)}")  # time of last access
    print(f"ST_MTIME = {dt.fromtimestamp(info.st_mtime)}")  # time of last modification
    print(f"ST_CTIME = {dt.fromtimestamp(info.st_ctime)}")  # creation time on windows/metadata change time on other systems like Unix

    # Get all files in directory and print most recently modified file
    files = [os.scandir("..")]



    # TODO: get all files in directory sorted by most recent last modified time
    # first
    # TODO: print all files in directory ordered by most recent time first



    # os.scandir()[0].stat().st_mtime
    # pathlib.Path.iterdir()[0].stat()
    # os.mkdir()
    # pathlib.Path.mkdir()
    # os.makedirs()
    # pathlib.Path.mkdir(parents = True)
    # fnmatch.fnmatch
    # glob.glob
    # glob.iglob
    # pathlib.Path.glob
    # os.walk
    # os.path.dirname
    # os.path.realpath
