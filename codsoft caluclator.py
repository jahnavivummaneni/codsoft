import tkinter as tk
from tkinter import messagebox

def button_click(symbol):
    current_text = entry_display.get()
    if current_text == "Error":
        entry_display.delete(0, tk.END)
        current_text = ""
    if symbol == "=":
        try:
            result = eval(current_text)
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, str(result))
        except Exception as e:
            entry_display.delete(0, tk.END)
            entry_display.insert(tk.END, "Error")
            messagebox.showerror("Error", "Invalid expression!")
    elif symbol == "C":
        entry_display.delete(0, tk.END)
    else:
        entry_display.insert(tk.END, symbol)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Entry field for display
entry_display = tk.Entry(root, width=30, font=("Arial", 14), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root,
        text=button,
        width=5,
        font=("Arial", 14),
        command=lambda b=button: button_click(b)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
