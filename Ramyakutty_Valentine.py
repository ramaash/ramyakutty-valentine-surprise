import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("Ramyakutty ❤️ Valentine Surprise")
root.geometry("500x400")
root.configure(bg="#ffe6f0")

label = tk.Label(root, text="Initializing Love Protocol...", 
                 font=("Arial", 16), bg="#ffe6f0")
label.pack(pady=40)

root.update()
time.sleep(2)

label.config(text="Scanning for Ramyakutty...")
root.update()
time.sleep(2)

label.config(text="Heart Match Found 💖")
root.update()
time.sleep(2)

def next_prompt():
    messagebox.showinfo("Prompt 1 💕",
                        "Do you remember the moment you first stole my heart?")
    messagebox.showinfo("Prompt 2 💕",
                        "When you smile at me, my entire world _______.")
    messagebox.showinfo("Prompt 3 💕",
                        "In every lifetime, I would still choose _______.")
    messagebox.showinfo("Final Output 💘",
                        "Ramyakutty...\n\n"
                        "You are my safest place.\n"
                        "You are my favorite notification.\n"
                        "You are my forever Valentine.\n\n"
                        "I love you. Always.\n\n- Ashwin ❤️")
    root.destroy()

button = tk.Button(root, text="Click to Continue 💖",
                   command=next_prompt,
                   font=("Arial", 14),
                   bg="#ff66b2",
                   fg="white")
button.pack(pady=40)

root.mainloop()

