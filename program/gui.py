import os
import tkinter.filedialog
def GUI_select_directory()->str:
    iDir = os.path.abspath(os.path.dirname(__file__))
    selected_file_path = tkinter.filedialog.askdirectory(initialdir = iDir)
    return  selected_file_path