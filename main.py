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
def start_app():
    os.system("python mani.py")

# Load and place the image in the center
image = PhotoImage(file="tech.png")  # Replace with your image path
image_label = tk.Label(root, image=image)
image_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create a "Start" button
start_button = tk.Button(root, text="Start", command=start_app, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
