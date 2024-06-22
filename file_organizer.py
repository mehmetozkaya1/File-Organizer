# Importing necessary libraries
import os
from tkinter import *
from tkinter import filedialog, messagebox
import shutil

# Creating a Tk() instance
gui = Tk()

# Needed file_types list and file_extensions dictionary
file_types = ["music", "word", "excel", "powerpoint", "software", "images", "videos" ,"pdf", "text", "zip", "apps"]
file_extensions = {"music": [".mp3", ".wav"], "word": [".docx", ".doc"], "excel": [".xls", ".xlsx", ".csv"], "powerpoint": [".ppt", ".pptx"], "software": [".c", ".py", ".js", ".html", ".css", ".cs", ".cpp"], "images": [".jpeg", ".jpg", ".png", ".ico"], "videos": [".mp4", ".mkv", ".webm", ".mov", ".avi", ".gif"], "pdf": [".pdf", ".PDF"], "text": [".txt", ".xml", ".rtf"], "zip": [".zip", ".rar"], "apps": [".exe"]}

# Creating FileOrganizer App Class
class FileOrganizer(Tk):
    def __init__(self):
        # General adjustments
        gui.title("File Organizer")
        gui.resizable(False, False)
        self.canvas = Canvas(gui, width = 400, height = 200)
        self.canvas.pack()

        # Frame
        self.frame = Frame(gui, width = 360, height = 190, bg = "#2d4245")
        self.frame.place(x = 20, y = 10)

        # Elements
        self.label = Label(self.frame, fg = "black", font = ("Microsoft YaHei UI Light", 11), width = 35, height = 1, text = "Please enter the file path to organise")
        self.label.place(x = 20, y = 15)

        self.button = Button(self.frame, border=0, width=26, font=("Microsoft YaHei UI Light",14,"bold"), bg="#6192ba", fg="black", text="Choose file path", command=self.select_path)
        self.button.place(x = 21, y = 50)

        self.path_label = Label(self.frame, fg = "black", font = ("Microsoft YaHei UI Light", 11), width = 35, height = 1, text = "...")
        self.path_label.place(x = 20, y = 100)

        self.organize_button = Button(self.frame, border=0, width=26, bg="#6192ba", font=("Microsoft YaHei UI Light",14,"bold"), fg="black", text="Organize", command=self.organise_path)
        self.organize_button.place(x = 21, y = 135)

    # A method to select the path
    def select_path(self):
        self.path = filedialog.askdirectory()
        self.path_label.config(text=str(self.path))

    def organise_path(self):
        # Change os path and create new folders if files exists
        os.chdir(self.path)

        # Create 'Folders' folder
        if not os.path.exists(self.path + "/" + "Folders"):
            os.mkdir("Folders")

        for file in os.listdir():
            (file_name, ext) = os.path.splitext(file)
            for file_type in file_types:
                # Create new folders if files exists
                for file_ext in file_extensions[file_type]:
                    if ext == file_ext:
                        if not os.path.exists(self.path + "/" + file_type.capitalize()):
                            os.mkdir(f"{file_type.capitalize()}")

                        # Move files to new folders
                        shutil.move(f"{self.path}/{file_name}{ext}", f"{self.path}/{file_type.capitalize()}")
        
        # Move existing folders to the 'Folders' folder
        for file_type in file_types:
            if os.path.exists(f"{self.path}/{file_type.capitalize()}"):
                shutil.move(f"{self.path}/{file_type.capitalize()}", f"{self.path}/Folders")
        
        # Inform user
        messagebox.showinfo("Success!", "Selected path organised successfully!")

# Create an FileOrganizer instance
file_organizer = FileOrganizer()
gui.mainloop()