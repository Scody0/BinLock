import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def encrypt_decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        file_data = f.read()

    key_bytes = key.encode('utf-8')
    encrypted_data = bytearray()
    for i in range(len(file_data)):
        encrypted_data.append(file_data[i] ^ key_bytes[i % len(key_bytes)])

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def select_file(action):
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        output_file = filedialog.asksaveasfilename(title="Save as", defaultextension=".dat")
        if output_file:
            key = entry_key.get()
            if key:
                encrypt_decrypt(file_path, output_file, key)
                messagebox.showinfo("Success", f"File {action} successfully!")
            else:
                messagebox.showwarning("Warning", "Please enter a key!")
        else:
            messagebox.showwarning("Warning", "Please choose a location to save the file!")
    else:
        messagebox.showwarning("Warning", "Please select a file!")

def on_enter(e):
    e.widget.config(style='Hover.TButton')

def on_leave(e):
    e.widget.config(style='Rounded.TButton')

root = tk.Tk()
root.title("BinLock - File Encryption/Decryption v0.0.1 beta")
root.geometry("400x300")

style = ttk.Style()
style.theme_use('clam')
style.configure("Rounded.TButton", padding=6, relief="flat", background="#007BFF", foreground="white", borderwidth=0)
style.configure("Hover.TButton", padding=6, relief="flat", background="#007BFF", foreground="black", borderwidth=0)
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 12))
style.configure("TEntry", fieldbackground="#2E2E2E", foreground="white")
style.configure("TFrame", background="#2E2E2E")

root.configure(bg="#2E2E2E")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(expand=True)

label_key = ttk.Label(frame, text="Enter encryption key:")
label_key.pack(pady=10)

entry_key = ttk.Entry(frame, show="*")
entry_key.pack(pady=5)

def create_rounded_button(parent, text, command):
    button = ttk.Button(parent, text=text, command=command, style="Rounded.TButton")
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack(pady=10, ipadx=10, fill='x', expand=True)
    return button

btn_encrypt = create_rounded_button(frame, "Encrypt File", lambda: select_file("encrypted"))
btn_decrypt = create_rounded_button(frame, "Decrypt File", lambda: select_file("decrypted"))

label_version = ttk.Label(frame, text="Version: v0.0.1 beta", background="#2E2E2E", foreground="white", font=("Helvetica", 10))
label_version.pack(pady=5)

label_developer = ttk.Label(frame, text="Developed by Scody", background="#2E2E2E", foreground="white", font=("Helvetica", 10))
label_developer.pack(pady=5)

root.mainloop()
