# Runs with pwsh
#exec(open("main.py").read())
import os
import pathlib
import shutil
import stat # To interpret results of os.stat()
import sys
import glob
from datetime import datetime as dt
from typing import List, Generator, Tuple, Set
from functools import reduce

def os_walk_print(g: Generator[Tuple[str, List[str], List[str]], None, None],
                  depth: int = 0,
                  space: str = "    ",
                  ignore_dirs: Set[str] = None,
                  output: str = "./os_walk/output.txt"):
    """
    A function that takes the generator returned by os.walk and prints results
    """
    try:
        node: Tuple[str, List[str], List[str]] = next(g)
        directory = node[0]
        directories = node[1]
        files = node[2]

        # Handle no ignore list
        if not ignore_dirs:
            ignore_dirs = set()

        # Check if directory should be ignored
        ignore = False
        for dir in ignore_dirs:
            # if directory.startswith(dir) or\
            #     directory.endswith(dir):
            if directory.startswith(dir):
                ignore = True
                break

        if not ignore:
            # Compute indentation
            prefix = ""
            for _ in range(depth):
                prefix = f"{prefix}|{space}"

            # Buffer lines in a list before writing
            # Path of current directory
            lines = [f"{prefix}{directory}\n"]

            # Add one more level of indentation for children
            prefix = f"{prefix}|{space}"
            if files:
                for file in files:
                    lines.append(f"{prefix}{file}\n")

            # Output to file
            mode = "at"
            if depth == 0:
                mode = "wt"
            with open(output, mode) as fl:
                fl.writelines(lines)

        # Recursively call on child directories
        for _ in directories:
            os_walk_print(g, depth = depth + 1, ignore_dirs = ignore_dirs)
    except StopIteration:
        # No more nodes to process
        pass

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
    files = list(filter(lambda x: x.is_file(), results))
    dirs = list(filter(lambda x: x.is_dir(), results))
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

    # Get a list of all files in a directory using pathlib
    # pathlib.Path().iterdir() returns a generator whose elements are either
    # PosixPath or WindowsPath
    print("----------------------------------------")
    print("  pathlib.Path().iterdir()")
    print("----------------------------------------")
    results: Generator[pathlib.WindowsPath, None, None] = pathlib.Path(repo_root_path).iterdir()
    results: List[pathlib.WindowsPath] = list(results)
    dirs = filter(lambda x: x.is_dir(), results)
    files = filter(lambda x: x.is_file(), results)
    print("Directories:")
    list(map(lambda x: print(f"    {x}"), sorted(dirs)))
    print("Files:")
    list(map(lambda x: print(f"    {x}"), sorted(files)))
    print("\n\n")
    # See documentation for PurePath/Path for more methods and properties.

    print("----------------------------------------")
    print("  File Attributes")
    print("----------------------------------------")
    # Get file attributes
    info = os.stat(this_file_path)
    mode = info.st_mode
    print(f"Attributes of {this_file_path}")
    print(f"    S_ISDIR = {stat.S_ISDIR(mode)}")                # file is a directory
    print(f"    S_ISREG = {stat.S_ISREG(mode)}")                # file is a regular file
    print(f"    ST_SIZE = {info.st_size}")                      # size of the file in bytes
    print(f"    ST_ATIME = {dt.fromtimestamp(info.st_atime)}")  # time of last access
    print(f"    ST_MTIME = {dt.fromtimestamp(info.st_mtime)}")  # time of last modification
    print(f"    ST_CTIME = {dt.fromtimestamp(info.st_ctime)}")  # creation time on windows/metadata change time on other systems like Unix
    print("\n\n")

    print("----------------------------------------")
    print("  List files in descending order of modified time")
    print("----------------------------------------")
    # Get all files in directory and print most recently modified file
    results: List[pathlib.WindowsPath] = list(pathlib.Path(repo_root_path).iterdir())
    files = list(filter(lambda x: x.is_file(), results))
    files_sorted = sorted(files, key = lambda x: x.stat().st_mtime, reverse = True)
    list(map(lambda x: print(f"    {dt.fromtimestamp(x.stat().st_mtime)}, {x}"), files_sorted))
    print("\n\n")

    print("----------------------------------------")
    print("  Recursively list files in a directory")
    print("----------------------------------------")
    # os.walk() returns a generator that yields a tuple
    # ret[0]: str - full path
    # ret[1]: List[str] - names of directory in path ret[0]
    # ret[2]: List[str] - file names in path ret[0]
    g = os.walk(repo_root_path)
    os_walk_print(g,
        ignore_dirs = {
            r"D:\src\learn-python\.git",
            r"D:\src\learn-python\__pycache__",
            r"env"
        })
    # for tpl in g:
    #     print(f"{directory_path}")
    #     directory_path = tpl[0]
    #     directories = tpl[1]
    #     files = tpl[2]


    sys.exit()
    # list(map(lambda x: print(f"    {x[0]}"), os.walk(repo_root_path)))
    # print(type(os.walk(repo_root_path)))
    results = os.walk(repo_root_path)
    for _ in range(2):
        x = next(results)
        print(x)
        print(type(x))

    print("----------------------------------------")
    print("  Pattern matching filenames")
    print("----------------------------------------")
    results: List[pathlib.WindowsPath] = list(pathlib.Path(repo_root_path).iterdir())




    print("----------------------------------------")
    print("  Directories")
    print("----------------------------------------")
    os_mkdir = f"{this_file_dir}\\os_mkdir"
    pathlib_mkdir = f"{this_file_dir}\\pathlib_mkdir"
    os_makedirs = f"{this_file_dir}\\os\\make\\dirs"
    pathlib_makedirs = f"{this_file_dir}\\path\\lib\\make\\dirs"

    # Create directories
    try:
        os.mkdir(os_mkdir)
        os.makedirs(os_makedirs)
    except FileExistsError:
        print(f"Directory {os_mkdir} already exists.")
    pathlib.Path(pathlib_mkdir).mkdir(exist_ok = True)
    pathlib.Path(pathlib_makedirs).mkdir(parents = True, exist_ok = True)

    # Check that directories are created


    # os.rmdir()
    # os.makedirs ()
    # pathlib.Path.mkdir(parents = True)

    # fnmatch.fnmatch
    # glob.glob
    # glob.iglob
    # pathlib.Path.glob
    # os.walk