import sys
import pathlib
from colorama import Fore, Style, init

init()

def list_directory_contents(path, indent_level=0):
    try:
        entries = list(path.iterdir())
    except Exception as e:
        print(Fore.RED + f"Error accessing {path}: {e}" + Style.RESET_ALL)
        return
    
    indent = '    ' * indent_level
    for entry in entries:
        if entry.is_dir():
            print(Fore.BLUE + f"{indent}{entry.name}/" + Style.RESET_ALL)
            list_directory_contents(entry, indent_level + 1)
        else:
            print(Fore.GREEN + f"{indent}{entry.name}" + Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = pathlib.Path(sys.argv[1])
    if not directory_path.is_dir():
        print(Fore.RED + "The provided path is not a directory or does not exist." + Style.RESET_ALL)
        sys.exit(1)
    
    list_directory_contents(directory_path)
