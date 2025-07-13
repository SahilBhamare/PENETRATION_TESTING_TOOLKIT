import socket
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
import threading
import queue

def launch():
    def start_scan():
        output.delete('1.0', tk.END)
        target = target_entry.get().strip()

        try:
            ip = socket.gethostbyname(target)
            output.insert(tk.END, f"[*] Scanning {ip}...\n")

            # Start background scan thread
            threading.Thread(target=scan_ports, args=(ip,), daemon=True).start()
            root.after(100, update_output_box)  # Schedule output updater

        except socket.gaierror:
            output.insert(tk.END, "[!] Invalid hostname or IP address\n")
        except Exception as e:
            output.insert(tk.END, f"[!] Error: {e}\n")

    def scan_ports(ip):
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1, 1025):
                executor.submit(scan_port, ip, port)

    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                result_queue.put(f"[+] Port {port} is OPEN")
            sock.close()
        except Exception as e:
            result_queue.put(f"[!] Error scanning port {port}: {e}")

    def update_output_box():
        try:
            while True:
                line = result_queue.get_nowait()
                output.insert(tk.END, line + "\n")
                output.see(tk.END)
        except queue.Empty:
            pass
        root.after(100, update_output_box)  # Keep checking for new output

    # ----- GUI Setup -----
    win = tk.Toplevel()
    win.title("Port Scanner")
    win.geometry("550x450")
    win.configure(bg="#393E46")

    tk.Label(win, text="Target Host/IP:", bg="#393E46", fg="white", font=("Arial", 12)).pack(pady=10)
    target_entry = tk.Entry(win, width=40, font=("Arial", 12))
    target_entry.pack(pady=5)

    scan_button = tk.Button(win, text="Start Scan", command=start_scan, bg="#00ADB5", fg="white", font=("Arial", 12, "bold"))
    scan_button.pack(pady=10)

    output = scrolledtext.ScrolledText(win, width=65, height=18, font=("Consolas", 10), bg="#222831", fg="#EEEEEE")
    output.pack(pady=10)

    result_queue = queue.Queue()  # Safe communication between threads
    root = win  # Used in root.after
