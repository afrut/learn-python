# Runs with pwsh
#exec(open("main.py").read())
import os
import pathlib
import shutil
import stat # To interpret results of os.stat()
import sys
from datetime import datetime as dt
from typing import List
if __name__ == "__main__":
    print("----------------------------------------")
    print("  Basics")
    print("----------------------------------------")
    # Get full path of this file
    # abspath resolves things like "." and ".." in the string passed in
    this_file_path: str = os.path.abspath(__file__)

    # Get directory of this file
    this_file_dir: str = os.path.dirname(__file__)

    # Get the full path of a file or directory, resolving symlinks if the OS
    # supports it
    resources_path: str = os.path.realpath(f"{this_file_dir}\\resources")

    # Get the root directory of the repository
    repo_root_path: str = os.path.abspath(f"{this_file_dir}\\..")

    # Append to a path
    file_name: str = os.path.join(resources_path, "plaintext.txt")

    print(f"this_file_path = {this_file_path}")
    print(f"this_file_dir = {this_file_dir}")
    print(f"resources_path = {resources_path}")
    print(f"repo_root_path = {repo_root_path}")
    print(f"file_name = {file_name}")
    print("\n\n")

    # Read file contents as text
    fl = open(file_name, "rt")
    contents = fl.read()
    print("----------------------------------------")
    print(f"  Contents of {file_name}")
    print("----------------------------------------")
    print(contents, end = "\n\n\n")
    fl.close()

    # Write text to a file
    some_str = "some trivial content"
    output_file_path: str = os.path.join(resources_path, "deleteme.txt")
    # with closes file after block ends
    with open(output_file_path, "wt") as fl:
        fl.write(some_str)
    with open(output_file_path, "rt") as fl:
        print("----------------------------------------")
        print(f"  Contents of {output_file_path}")
        print("----------------------------------------")
        print(fl.read())
    print("\n\n")

    # Get a list of all top-level files in a directory using os.listdir()
    # os.listdir() is for legacy versions
    dirs = []
    files = []
    dir_contents: List[str] = os.listdir(repo_root_path)
    print("----------------------------------------")
    print("  os.listdir()")
    print("----------------------------------------")
    for p in dir_contents:
        # Full path of file
        full_path = os.path.join(repo_root_path, p)

        # Append to different lists depending on whether or not the target is a
        # file or directory
        if os.path.isfile(full_path):
            files.append(full_path)
        if os.path.isdir(full_path):
            dirs.append(full_path)
    print("Directories:")
    list(map(lambda x: print(f"    {x}"), sorted(dirs))) # print contents of list
    print("Files:")
    list(map(lambda x: print(f"    {x}"), sorted(files)))
    print("\n\n")

    # Get a list of all files in a directory using os.scandir()
    # os.scandir() returns nt.ScandirIterator. Each element is type nt.DirEntry.
    # Prefer this over os.listdir(). Useful when the properties of each file
    # needs to be inspected in some way
    print("----------------------------------------")
    print("  os.scandir()")
    print("----------------------------------------")
    dir_contents = os.scandir(repo_root_path)
    results = []
    for p in os.scandir(repo_root_path):
        results.append(p)
    files = list(filter(lambda x: True if x.is_file() else False, results))
    dirs = list(filter(lambda x: True if x.is_dir() else False, results))
    print("Directories:")
    list(map(lambda x: print(f"    {x.path}"), sorted(dirs, key = lambda x: x.path)))
    print("Files:")
    list(map(lambda x: print(f"    {x.path}"), sorted(files, key = lambda x: x.path)))
    print("\n\n")
    # Other attributes that can be accessed
    # print(f"    name: {dir_entry.name}")
    # print(f"    path: {dir_entry.path}")
    # print(f"    inode(): {dir_entry.inode()}")
    # print(f"    is_dir(): {dir_entry.is_dir()}")
    # print(f"    is_file(): {dir_entry.is_file()}")
    # print(f"    is_symlink(): {dir_entry.is_symlink()}")
    # print(f"    stat(): {dir_entry.stat()}")
    sys.exit()

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
    info = os.stat(os.path.join(repo_root_path, "main.py"))
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
    # TODO : print all files in directory ordered by most recent time first



    # os.scandir()[0].stat().st_mtime
    # pathlib.Path.iterdir()[0].stat()
    # os.mkdir()
    # pathlib.Path.mkdir()
    # os.makedirs ()
    # pathlib.Path.mkdir(parents = True)
    # fnmatch.fnmatch
    # glob.glob
    # glob.iglob
    # pathlib.Path.glob
    # os.walk
