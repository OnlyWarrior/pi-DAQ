import tkinter as tk
from PIL import Image, ImageTk
import sys
import os
import subprocess
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg="black")
root.attributes('-fullscreen', True)

def exit_fullscreen_or_quit(event):
    if event.char.lower() == 'x':
        root.destroy()
        sys.exit()

def wait_for_key(root):
    var = tk.BooleanVar(root)

    def key_pressed(event):
        var.set(True)
        run_other_script()  # Call function to run the other script

    root.bind("<KeyPress>", key_pressed)
    root.wait_variable(var)
    root.unbind("<KeyPress>")

def run_other_script():
    # Ensure the correct Python interpreter is used
    python_interpreter = sys.executable  # This will use the currently active Python interpreter

    script_to_run = "grapher.py"  # Path to the other script
    try:
        # Use Popen to run the script without blocking the main thread
        subprocess.Popen([python_interpreter, script_to_run])
    except FileNotFoundError:
        print(f"Script '{script_to_run}' not found!")
    except Exception as e:
        print(f"Error occurred while running the script: {e}")

root.bind_all("<Key>", exit_fullscreen_or_quit)

if __name__ == '__main__':
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True)

    image = Image.open("IconClear.png")
    image = image.resize((600, 600), Image.ANTIALIAS)  # Resize if needed
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(frame, image=photo, bg="black")
    image_label.pack(pady=20)  # Space between image and text

    label = tk.Label(
        frame,
        text="Press any key",
        font=("Helvetica", 212),
        fg="white",
        bg="black",
        anchor="center"
    )
    label.pack()

    wait_for_key(root)
    label.config(text="Key pressed!")

    root.mainloop()
