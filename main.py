import os
import threading

from gui import GUI
from tkinter import messagebox, filedialog, PhotoImage
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

yt = None
streams = None
selected_stream = None
user_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")


def load_thread():
    def load_streams():
        global yt, streams
        try:
            yt = YouTube(gui.entry_url.get(),
                         on_complete_callback=download_complete,
                         on_progress_callback=download_in_progress)
            streams = yt.streams
        except VideoUnavailable:
            messagebox.showinfo(master=gui, title="ERROR", message="This video is not available.")
        except RegexMatchError:
            messagebox.showinfo(master=gui, title="ERROR", message="Invalid YouTube URL.")
        else:
            for stream in streams:
                if stream.includes_audio_track:
                    gui.stream_list.append(f"{stream.type.upper()} -- Type: {stream.subtype}, "
                                           f"Resolution: {stream.resolution}, "
                                           f"Quality: {stream.abr}, "
                                           f"itag: {stream.itag}")
            gui.combo_box.config(values=gui.stream_list, state="readonly")
    thread = threading.Thread(target=load_streams)
    thread.start()


def download_thread():
    if os.path.isdir(gui.entry_folder.get()):
        def download_stream():
            global selected_stream
            itag = gui.stream_selected.get().split("itag: ")[1]
            selected_stream = streams.get_by_itag(itag)
            selected_stream.download(output_path=gui.entry_folder.get())
        thread = threading.Thread(target=download_stream)
        thread.start()
    else:
        messagebox.showinfo(master=gui, title="ERROR", message=f"Invalid location: {gui.entry_folder.get()}")


def browse_button():
    folder = filedialog.askdirectory().replace("/", "\\")
    gui.entry_folder.delete(0, "end")
    gui.entry_folder.insert(0, folder)


def enable_download_button(*args):
    gui.button_download.config(state="active")


def download_complete(*args):
    messagebox.showinfo(master=gui, title="INFO", message=f"Downloaded to: {args[1]}")


def download_in_progress(*args):
    gui.progress_bar['value'] = 0
    bytes_remaining = args[2]
    percent = 100 - round((bytes_remaining / selected_stream.filesize_approx) * 100)
    gui.update_idletasks()
    gui.progress_bar['value'] = percent
    gui.button_download.config(state="disabled")

if __name__ == "__main__":
    gui = GUI()
    gui.entry_folder.insert(0, user_download_folder)
    gui.button_load.config(command=load_thread)
    gui.button_folder.config(command=browse_button)
    gui.stream_selected.trace("w", callback=enable_download_button)
    gui.button_download.config(command=download_thread)
    gui.mainloop()
