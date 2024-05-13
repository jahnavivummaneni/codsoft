import tkinter as tk
import random
import string

password = ""

def generate_password():
    global password
    try:
        if entry_username.get() and entry_length.get():
            length = int(entry_length.get())
            if length <= 0:
                password = "Invalid length! Please enter a positive integer."
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for i in range(length))
        elif entry_length.get():
            password = "Enter Username!"
        else:
            password = "Enter Desired Length of Password!"
    except ValueError:
        password = "Please enter a valid integer for the password length."
        
    label_generated.config(text="Generated Password: " + password)

def display_message():
    global password
    if password:
        message = "Hello " + entry_username.get() + "! Your password is: " + password
        label_message.config(text=message)
    else:
        label_message.config(text="No password generated yet!")

def clear_fields():
    entry_username.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    label_generated.config(text="")
    label_message.config(text="")

window = tk.Tk()
window.geometry('600x300')
window.title("Password Generator")

label_title = tk.Label(window, text="PASSWORD GENERATOR", font=("Rockwell", 24, "bold"))
label_title.pack(pady=10)

frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_username = tk.Label(frame_input, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)

entry_username = tk.Entry(frame_input)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_length = tk.Label(frame_input, text="Password Length:")
label_length.grid(row=1, column=0, padx=5, pady=5)

entry_length = tk.Entry(frame_input)
entry_length.grid(row=1, column=1, padx=5, pady=5)

button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.pack(pady=5)

label_generated = tk.Label(window, text="")
label_generated.pack(pady=5)

button_display = tk.Button(window, text="Display Message", command=display_message)
button_display.pack(pady=5)

label_message = tk.Label(window, text="")
label_message.pack(pady=5)

button_clear = tk.Button(window, text="Clear Fields", command=clear_fields)
button_clear.pack(pady=5)

window.mainloop()
