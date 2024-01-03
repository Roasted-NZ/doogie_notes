import tkinter as tk
from datetime import datetime
from pygame import mixer
import os

def save_entry():
    # Get the current date and time as a human readable format
    dt_string = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

    # Get the contents of the note field
    note = note_entry.get("1.0", "end").strip()

    # Create a directory to store the entries, if it doesn't exist already
    if not os.path.exists("Entries"):
        os.makedirs("Entries")

    # Create a file with the entry's date and time in the filename
    filename = f"Entries/ENTRY_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(f"{dt_string}\n\n\t{note}")

    # Clear the note field for the next entry
    note_entry.delete("1.0", "end")

def play_music():
    mixer.init()
    mixer.music.load("music.mp3")
    mixer.music.set_volume(0.3) # Set the volume to 30%
    mixer.music.play()

# Create the main window
root = tk.Tk()
root.geometry("1200x600")
root.configure(bg="#8da7ff")

# Create the date/time label
dt_label = tk.Label(root, text=datetime.now().strftime("%A, %B %d, %Y %I:%M %p"), font=("Lucida Console", 25), fg="#FFFFFF", bg="#8da7ff")
dt_label.pack(pady=50)

# Create the note entry field
note_entry = tk.Text(root, height=10, width=60, font=("Lucida Console", 20), bg="#003aff", fg="#FFFFFF", insertbackground="#FFFFFF", padx=10, pady=10)
note_entry.pack()

# Create the save button
save_button = tk.Button(root, text="SAVE", command=save_entry, font=("Lucida Console", 18), bg="#8da7ff", fg="#000000")
save_button.pack(side="right", pady=50)

# Play the music in the background
play_music()

root.mainloop()
