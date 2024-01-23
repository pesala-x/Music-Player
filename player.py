import os
import tkinter as tk
from tkinter import filedialog
import pygame
from pygame import mixer

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("500x300")

        self.tracklist = []
        self.current_track = 0
        self.paused = False

        mixer.init()  # Initialize Pygame mixer

        self.create_widgets()

    def create_widgets(self):
        # Song listbox
        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, width=40)
        self.listbox.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Buttons
        tk.Button(self.master, text="Add Songs", command=self.add_songs).grid(row=1, column=0, pady=10)
        tk.Button(self.master, text="Play", command=self.play_music).grid(row=1, column=1, pady=10)
        tk.Button(self.master, text="Pause/Resume", command=self.pause_resume_music).grid(row=1, column=2, pady=10)

    def add_songs(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        self.tracklist.extend(file_paths)

        for file_path in file_paths:
            song_name = os.path.basename(file_path)
            self.listbox.insert(tk.END, song_name)


# Create the Tkinter window
root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
