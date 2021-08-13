import tkinter as tk
from tkinter.constants import TOP, VERTICAL
from PIL import ImageTk, Image
from tkinter import filedialog
#from face_detection import face_detection

root = tk.Tk()
root.geometry("700x500") # the application window size
root.title("I need a NAME!") # title of window
#icon = 'icon.ico'
#root.iconphoto( False, icon ) # application icon

def file_dialog():
    filename = filedialog.askopenfilename(
        initialdir="Downloads",
        title="Select A File To Start",
        filetypes=(
            ("mp4 files", "*.mp4"),
            ("mov files", "*.mov"),
            ("png files", "*.png"),
            ("jpeg files", "*.jpeg"),
            ("jpg files", "*.jpg")))

    if filename:
        root.img = tk.PhotoImage(file=filename)

button = tk.Button(root, background="yellow", text="Choose A File", command=file_dialog)
button.grid(column=5, row=2)

#button = tk.Button(root, background="green", text="Face Detection", command=face_detection)

root.mainloop()

print("Successful Build")