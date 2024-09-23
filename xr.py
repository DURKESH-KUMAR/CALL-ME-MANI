import tkinter as tk
from tkinter import PhotoImage
import os

# Create the main window
root = tk.Tk()
root.title("Phone Display UI")
root.geometry("360x640")  # Standard phone display size (portrait mode)

# Set background color (optional)
root.configure(bg="black")

# Function to handle the button click

    

# Load and place the image in the center
image = PhotoImage(file="xr.png")  # Replace with your image path
image_label = tk.Label(root, image=image)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


# Run the Tkinter event loop
root.mainloop()
