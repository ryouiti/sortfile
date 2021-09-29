import os
import tkinter.filedialog
import ctypes
def GUI_select_directory()->str:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)#DPIを調節してエクスプローラーの解像度を上げる  MAC環境では使えない 
    iDir = os.path.abspath(os.path.dirname(__file__))
    selected_file_path = tkinter.filedialog.askdirectory(initialdir = iDir)
    return  selected_file_path
GUI_select_directory()