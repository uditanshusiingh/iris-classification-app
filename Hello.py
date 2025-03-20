import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My GUI App")

# Add widgets
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

def button_click():
    label.config(text="Button clicked!")

button = tk.Button(window, text="Click Me!", command=button_click)
button.pack()

# Start the main event loop
window.mainloop()
