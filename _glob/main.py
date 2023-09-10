# Pattern matching file paths and names using Unix shell rules
import glob
import os

if __name__ == "__main__":
    # Get root of the repository via relative directory
    this_file = os.path.abspath(__file__)
    this_file_dir = os.path.dirname(this_file)
    repo_root = os.path.abspath(f"{this_file_dir}\\..")

    # All files under a directory
    pattern = f"{repo_root}\\*"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern))))
    print("")

    # All files under a directory matching an extension
    pattern = f"{repo_root}\\*.py"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern))))
    print("")

    # All directories in a current directory
    pattern = f"{repo_root}\\**\\"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern))))
    print("")

    # All files and subdirectories in a directory and it subdirectories
    pattern = f"{repo_root}\\.git\\**"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern, recursive = True))))
    print("")

    # All subdirectories with the name env
    pattern = f"{repo_root}\\**\\env"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern, recursive = True))))
    print("")

    # All files and subdirectories of subdirectories named env anywhere in the path
    pattern = f"{repo_root}\\**\\env\\**"
    print(pattern)
    list(map(lambda x: print(f"    {x}"), sorted(glob.glob(pattern, recursive = True))))
    print("")