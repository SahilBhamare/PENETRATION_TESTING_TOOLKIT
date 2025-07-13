import tkinter as tk
from tkinter import scrolledtext
import time

# Simulated brute-force attack using a wordlist
def launch():
    def start_attack():
        output.delete('1.0', tk.END)
        username = user_entry.get()
        target_pass = pass_entry.get()
        found = False

        try:
            with open("assets/wordlist.txt", "r") as f:
                for pwd in f:
                    pwd = pwd.strip()
                    output.insert(tk.END, f"Trying password: {pwd}\n")
                    output.update()
                    time.sleep(0.1)
                    if pwd == target_pass:
                        output.insert(tk.END, f"\n[✔] Password found for {username}: {pwd}\n")
                        found = True
                        break

            if not found:
                output.insert(tk.END, f"\n[✘] Password not found.\n")

        except FileNotFoundError:
            output.insert(tk.END, "[!] Wordlist file not found (assets/wordlist.txt)")

    win = tk.Toplevel()
    win.title("Brute Force Simulator")
    win.geometry("500x450")
    win.configure(bg="#222831")

    tk.Label(win, text="Username", bg="#222831", fg="#EEEEEE").pack(pady=5)
    user_entry = tk.Entry(win, width=40)
    user_entry.pack()

    tk.Label(win, text="Target Password (for testing)", bg="#222831", fg="#EEEEEE").pack(pady=5)
    pass_entry = tk.Entry(win, width=40, show="*")
    pass_entry.pack()

    tk.Button(win, text="Start Brute Force", command=start_attack, bg="#00ADB5", fg="white").pack(pady=10)

    output = scrolledtext.ScrolledText(win, width=60, height=15)
    output.pack(pady=10)
