import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ScheduleMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Autism-Friendly Schedule Maker")

        # List to hold the schedule entries
        self.schedule = []

        # Frame for schedule input
        self.frame_input = tk.Frame(root)
        self.frame_input.pack(pady=10)

        # Task Label and Entry
        self.label_task = tk.Label(self.frame_input, text="Task:")
        self.label_task.grid(row=0, column=0)
        self.entry_task = tk.Entry(self.frame_input, width=30)
        self.entry_task.grid(row=0, column=1)

        # Button to choose an image
        self.button_image = tk.Button(self.frame_input, text="Choose Image", command=self.choose_image)
        self.button_image.grid(row=1, column=0, columnspan=2, pady=5)

        # Button to add task to the schedule
        self.button_add = tk.Button(self.frame_input, text="Add to Schedule", command=self.add_to_schedule)
        self.button_add.grid(row=2, column=0, columnspan=2, pady=5)

        # Frame for displaying the schedule
        self.frame_schedule = tk.Frame(root)
        self.frame_schedule.pack(pady=10)

        # Button to display the schedule
        self.button_display = tk.Button(root, text="Display Schedule", command=self.display_schedule)
        self.button_display.pack(pady=5)

    def choose_image(self):
        # Open file dialog to choose an image
        self.image_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),)
        )
        if self.image_path:
            self.label_image_chosen = tk.Label(self.frame_input, text=os.path.basename(self.image_path))
            self.label_image_chosen.grid(row=1, column=1)

    def add_to_schedule(self):
        # Get task and image path
        task = self.entry_task.get()
        if task and hasattr(self, 'image_path'):
            # Append task and image to the schedule
            self.schedule.append((task, self.image_path))
            # Clear the task entry and reset the image path
            self.entry_task.delete(0, tk.END)
            self.label_image_chosen.grid_forget()

    def display_schedule(self):
        # Clear the frame for displaying the schedule
        for widget in self.frame_schedule.winfo_children():
            widget.destroy()

        # Display each task with its corresponding image
        for i, (task, image_path) in enumerate(self.schedule):
            label_task = tk.Label(self.frame_schedule, text=task, font=("Arial", 14))
            label_task.grid(row=i, column=0, padx=10, pady=5)

            img = Image.open(image_path)
            img = img.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)

            label_image = tk.Label(self.frame_schedule, image=img)
            label_image.image = img  # Keep a reference to avoid garbage collection
            label_image.grid(row=i, column=1, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleMaker(root)
    root.mainloop()
