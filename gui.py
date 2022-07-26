

import pyscreenrec
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

rec=pyscreenrec.ScreenRecorder()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start_rec():
    file =Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
def stop_rec():
    rec.stop_recording()

window = Tk()
window.title("Quick Screen Recorder")
window.geometry("600x150")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 150,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    295.0,
    40.0,
    image=image_image_1
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start_rec,
    relief="flat"
)


button_1.place(
    x=62.0,
    y=75.46883392333984,
    width=45.077056884765625,
    height=46.14019775390625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=resume_rec,
    relief="flat"
)
button_2.place(
    x=135.77452087402344,
    y=76.55374908447266,
    width=44.43916320800781,
    height=47.878379821777344
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=stop_rec,
    relief="flat"
)
button_3.place(
    x=208.0035858154297,
    y=75.0,
    width=45.50230407714844,
    height=44.439170837402344
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=pause_rec,
    relief="flat"
)
button_4.place(
    x=281.1537170410156,
    y=75.46883392333984,
    width=45.077056884765625,
    height=44.439170837402344
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    468.5,
    103.5,
    image=entry_image_1
)

Filename=StringVar()
entry_1 = Entry(textvariable=Filename,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    
)

entry_1.place(
    x=372.0,
    y=92.0,
    width=193.0,
    height=25.0
)
Filename.set("Untitled Recording")
window.resizable(False, False)
window.mainloop()
