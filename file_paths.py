
import tkinter as tk
from tkinter import filedialog
import os

def select_file(window_title: str = "Select a file", file_type: tuple[str,str] = ("TXT files", "*.txt")) -> str:
    """
    Opens a file selection dialog to allow the user to choose a file. 
    The dialog starts in the current working directory and filters file types to `.txt` files by default.

    Args:
        window_title (str): The title of the file selection dialog window. Defaults to "Select a file".

    Returns:
        str: The full path of the selected file as a string. If the user cancels the selection, an empty string is returned.

    Notes:
        - The function hides the root `tkinter` window.
        - The dialog restricts the file selection to `.txt` files by default, but allows selecting any file type.
        - The initial directory is set to the current working directory.
    """ 
    # Create a root window (it won't be displayed)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Set the title of the file dialog window
    root.title(window_title)

    # Get the current working directory
    current_dir = os.getcwd()

    # Open a file dialog and store the selected file path
    file_path = filedialog.askopenfilename(
        title=window_title,
        initialdir=current_dir,  # Set the dialog to open in the current directory
        filetypes=[file_type, ("All files", "*.*")]  
    )

    # Return the file path
    return file_path


def select_save_file_path(default_name: str = "untitled.txt", save_dir: str = os.getcwd()) -> str:
    """
    Opens a "Save As" dialog to allow the user to select a file path and filename for saving a file.
    The dialog will start in a specified directory and suggest a default filename and file type (.txt).

    Args:
        default_name (str): The default file name to suggest in the "Save As" dialog. Defaults to "untitled.txt".
        save_dir (str): The directory to open the dialog in. Defaults to the current working directory.

    Returns:
        str: The full path of the selected file, including the file name and extension. If the user cancels
             the operation, an empty string is returned.

    Notes:
        - The function hides the root `tkinter` window.
        - The dialog filters the file types, showing `.txt` files by default, but allows selecting any file type.
        - The `.txt` extension is added automatically if the user does not specify one.
    """

    # Create a root window (it won't be displayed)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a save file dialog and get the selected file path
    file_path = filedialog.asksaveasfilename(
        title="Save As",
        initialdir=save_dir,
        initialfile=default_name,
        defaultextension="txt",  # Add the default extension
        filetypes=[("TXT files", "*.txt"), ("All files", "*.*")]  # Restrict file types
    )

    # Return the selected file path
    return file_path
