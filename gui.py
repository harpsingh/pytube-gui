import os
import sys
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar


# https://stackoverflow.com/questions/51060894/adding-a-data-file-in-pyinstaller-using-the-onefile-option
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.config(padx=20, pady=10)
        self.geometry("500x350")
        download_icon = PhotoImage(file=resource_path("images/download.png"))
        self.iconphoto(False, download_icon)

        self.label_url = Label(self, text="Paste YouTube URL here:", font=("Arial", 10))
        self.label_url.pack(anchor="w")
        self.entry_url = Entry(self, borderwidth=2, font=("Arial", 9))
        self.entry_url.pack(fill="x")
        self.button_load = Button(self, text="Load")
        self.button_load.pack(anchor="e", pady=5)

        self.label_folder = Label(self, text="Download location:", font=("Arial", 9))
        self.label_folder.pack(anchor="w")
        self.entry_folder = Entry(self, borderwidth=2, font=("Arial", 9))
        self.entry_folder.pack(fill="x")
        self.button_folder = Button(self, text="Browse")
        self.button_folder.pack(anchor="e", pady=5)

        self.spacer1 = Label(self, text="")
        self.spacer1.pack()

        self.label_stream = Label(self, text="Select stream to download:", font=("Arial", 10))
        self.label_stream.pack(anchor="w")
        self.stream_selected = StringVar()
        self.stream_list = []
        self.combo_box = ttk.Combobox(state="disabled", textvariable=self.stream_selected)
        self.combo_box.pack(anchor="w", fill="x")

        self.button_download = Button(self, text="Download", state="disabled")
        self.button_download.pack(anchor="e", pady=10)

        self.progress_bar = Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate')
        self.progress_bar.pack(fill="x")

        self.label_credit = Label(self, text="https://github.com/harpsingh/pytube-gui",
                                  font=("Arial", 9, "underline"), fg="blue")
        self.label_credit.pack(anchor="w", pady=10)
        self.label_credit.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/harpsingh/pytube-gui"))
