import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x500")
        self.filename = None
        self.text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", 12))
        self.text_area.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.event_generate("<<SelectAll>>"))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        root.config(menu=menu_bar)

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.filename = None
        self.root.title("Notepad")
    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.filename = file
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, content)
            self.root.title(f"Notepad - {file}")

    def save_file(self):
        if self.filename:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Notepad", "File saved successfully.")
        else:
            self.save_as()

    def save_as(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.filename = file
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END))
            self.root.title(f"Notepad - {file}")
            messagebox.showinfo("Notepad", "File saved successfully.")

root = tk.Tk()
app = Notepad(root)
root.mainloop()