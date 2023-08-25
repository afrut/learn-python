#exec(open("working_with_files.py").read())
import os # https://docs.python.org/3/library/os.html
import pathlib
import shutil
if __name__ == "__main__":
    file_path = ".\\resources\\"

    # Get full path of a directory
    dir_path = os.path.abspath(".\\")
    #print(f"Full path: {dir_path}")

    # Read file contents as text
    file_name = f"{file_path}plaintext.txt"
    fl = open(file_name, "rt")
    contents = fl.read()
    fl.close()

    print("----------------------------------------")
    print(f"  Contents of {file_name}")
    print("----------------------------------------")
    print(contents, end = "\n\n\n")

    # Write text to file
    some_str = "some trivial content"
    # with close closes file
    with open(f"{file_path}deleteme.txt", "wt") as fl:
        fl.write(some_str)

    # Get a list of all files in a directory
    print("----------------------------------------")
    print(f"  Contents of {dir_path}")
    print("----------------------------------------")
    # listdir is for legacy versions
    #for x in os.listdir(dir_path):
    #    print(f"{dir_path}{x}")
    for dir_entry in os.scandir(dir_path):
        print(f"Name: {dir_entry.name}")
        print(f"    path: {dir_entry.path}")
        print(f"    inode(): {dir_entry.inode()}")
        print(f"    is_dir(): {dir_entry.is_dir()}")
        print(f"    is_file(): {dir_entry.is_file()}")
        print(f"    is_symlink(): {dir_entry.is_symlink()}")
        print(f"    stat(): {dir_entry.stat()}")

    pathlib.Path.iterdir()
    os.path.isfile
    os.path.isdir()
    os.path.join()
    os.scandir()[0].stat().st_mtime
    pathlib.Path.iterdir()[0].stat()
    os.mkdir()
    pathlib.Path.mkdir()
    os.makedirs()
    pathlib.Path.mkdir(parents = True)
    fnmatch.fnmatch
    glob.glob
    glob.iglob
    pathlib.Path.glob
    os.walk
    os.path.dirname
    os.path.realpath
