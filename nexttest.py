import tkinter as tk
from tkinter import filedialog, messagebox, font, colorchooser

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File has been saved successfully!")

def exit_app():
    window.destroy()

def change_font(font_name):
    text_area.config(font=(font_name, 12))

def change_text_color():
    color = colorchooser.askcolor(title="Choose text color")[1]
    if color:
        text_area.config(fg=color)

def change_bg_color():
    color = colorchooser.askcolor(title="Choose background color")[1]
    if color:
        text_area.config(bg=color)

def enable_dark_mode():
    window.config(bg="#2e2e2e")
    text_area.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white")
    menu_bar.config(bg="#2e2e2e", fg="white")

# Main window
window = tk.Tk()
window.title("Advanced NotePad")
window.geometry("700x500")

# Text area
text_area = tk.Text(window, font=("Arial", 12), wrap="word", undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

# Menu
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu = tk.Menu(menu_bar, tearoff=0)
font_menu = tk.Menu(menu_bar, tearoff=0)

# File menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Font options
fonts = ["Arial", "Courier New", "Times New Roman", "Comic Sans MS", "Helvetica"]
for f in fonts:
    font_menu.add_command(label=f, command=lambda f=f: change_font(f))

# Theme menu
theme_menu.add_command(label="Dark Mode", command=enable_dark_mode)
theme_menu.add_command(label="Text Color", command=change_text_color)
theme_menu.add_command(label="Background Color", command=change_bg_color)

# Adding to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Fonts", menu=font_menu)
menu_bar.add_cascade(label="Themes", menu=theme_menu)

window.config(menu=menu_bar)

# Run
window.mainloop()
