from ast import Lambda
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[('Text Files', "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, 'r') as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[('Text Files', "*.txt")])    

    if not filepath:
        return
    
    with open(filepath, 'w') as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Text Editor") 
    window.rowconfigure(0, minsize=400)  # Configure the minimum size of the row at index 0
    window.columnconfigure(1, minsize=500)  # Configure the minimum size of the column at index 1

    # Create a Text widget for the main text editing area
    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)  # Place the Text widget in the grid at row 0, column 1

    # Create a frame to hold buttons (Save and Open)
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    
    # Create Save and Open buttons
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    # Place Save and Open buttons in the grid inside the frame
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    open_button.grid(row=1, column=0, padx=5, sticky='ew')
    
    # Place the frame in the grid at row 0, column 0, and make it sticky to the north-south direction
    frame.grid(row=0, column=0, sticky="ns")

    # Configure keyboard shortcuts
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))


    window.mainloop()


main()
