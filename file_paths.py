import tkinter as tk
from tkinter import filedialog
import os
from typing import List, Tuple, Union

def create_hidden_root() -> tk.Tk:
    """
    Creates and returns a hidden Tkinter root window.

    Returns:
        tk.Tk: A hidden Tkinter root window.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    return root

def select_file(
    window_title: str = "Select a file", 
    file_types: Union[ List[Tuple[str, str]] , None ]= None,
    initial_dir: Union[ str , None ] = None
) -> str:
    """
    Opens a file selection dialog for the user to choose a file.

    Args:
        window_title (str): Title of the file selection dialog window. Defaults to "Select a file".
        file_types (List[Tuple[str, str]]): A list of tuples specifying file type filters. Defaults to TXT files.
        initial_dir (str): Initial directory for the dialog. Defaults to the current working directory.

    Returns:
        str: Full path of the selected file. Returns an empty string if canceled.
    """
    root = create_hidden_root()

    # Add "All Files" option if not already present
    file_types = file_types or [("TXT files", "*.txt"), ("All files", "*.*")]
    if ("All files", "*.*") not in file_types:
        file_types.append(("All files", "*.*"))
    
    # Automatically combine extensions into a "combined filter"
    combined_extensions = " ".join(ft[1] for ft in file_types if ft[1] != "*.*")
    if combined_extensions:
        file_types.insert(0, ("Supported files", combined_extensions))

    file_path = filedialog.askopenfilename(
        title=window_title,
        initialdir=initial_dir or os.getcwd(),
        filetypes=file_types
    )
    return file_path

def select_save_file_path(
    window_title: str = "Save As",
    default_name: str = "untitled.txt",
    file_types: List[Tuple[str, str]] = [("TXT files", "*.txt"), ("All files", "*.*")],
    initial_dir: str = os.getcwd(),
    default_extension: str = "txt"
) -> str:
    """
    Opens a "Save As" dialog for the user to select a file path and name for saving a file.

    Args:
        window_title (str): Title of the save dialog window. Defaults to "Save As".
        default_name (str): Default file name suggested in the dialog. Defaults to "untitled.txt".
        file_types (List[Tuple[str, str]]): A list of tuples specifying file type filters. Defaults to TXT files.
        initial_dir (str): Initial directory for the dialog. Defaults to the current working directory.
        default_extension (str): Default file extension if the user doesn't specify one. Defaults to "txt".

    Returns:
        str: Full path of the selected file, including name and extension. Returns an empty string if canceled.
    """
    root = create_hidden_root()
    file_path = filedialog.asksaveasfilename(
        title=window_title,
        initialdir=initial_dir,
        initialfile=default_name,
        defaultextension=default_extension,
        filetypes=file_types
    )
    return file_path
