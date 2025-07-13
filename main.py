import tkinter as tk
from tkinter import messagebox, ttk
from modules import port_scanner, brute_forcer

# Main GUI Window
class PenTestToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penetration Testing Toolkit")
        self.root.geometry("600x400")
        self.root.configure(bg="#222831")

        self.title = tk.Label(root, text="🛠️ Penetration Testing Toolkit", font=("Helvetica", 18, "bold"), fg="#00ADB5", bg="#222831")
        self.title.pack(pady=20)

        self.desc = tk.Label(root, text="Select a tool below:", font=("Helvetica", 14), fg="#EEEEEE", bg="#222831")
        self.desc.pack(pady=10)

        # Dropdown menu to choose tools
        self.options = ["Port Scanner", "Brute Force (SSH Sim)"]
        self.combo = ttk.Combobox(root, values=self.options, state="readonly")
        self.combo.current(0)
        self.combo.pack(pady=10)

        self.start_btn = tk.Button(root, text="Launch Tool", command=self.launch_tool, bg="#00ADB5", fg="white", font=("Arial", 12, "bold"))
        self.start_btn.pack(pady=20)

    def launch_tool(self):
        tool = self.combo.get()
        if tool == "Port Scanner":
            port_scanner.launch()
        elif tool == "Brute Force (SSH Sim)":
            brute_forcer.launch()
        else:
            messagebox.showwarning("Invalid", "Tool not found.")

# Run the main app
if __name__ == "__main__":
    root = tk.Tk()
    app = PenTestToolkitApp(root)
    root.mainloop()



