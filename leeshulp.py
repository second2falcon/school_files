import tkinter as tk
from tkinter import ttk
from tkinter import StringVar

class WordFlasherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Flasher")

        self.text_entry = tk.Entry(root, font=("Arial", 16))
        self.text_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.time_label = tk.Label(root, text="Time per word (s):")
        self.time_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.time_value = StringVar()
        self.time_value.set("0.50")
        self.time_slider = ttk.Scale(root, from_=0.05, to=1.0, orient="horizontal", length=300, variable=self.time_value, command=self.update_slider)
        self.time_slider.set(0.50)
        self.time_slider.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.time_display_label = tk.Label(root, textvariable=self.time_value)
        self.time_display_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.font_size_label = tk.Label(root, text="Character Size:")
        self.font_size_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.font_size_value = StringVar()
        self.font_size_value.set("24")
        self.font_size_entry = ttk.Entry(root, textvariable=self.font_size_value)
        self.font_size_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.display_mode_var = tk.IntVar()  # 0 for black text on grey, 1 for white text on black
        self.display_mode_checkbutton = ttk.Checkbutton(root, text="White Text on Black", variable=self.display_mode_var, command=self.toggle_display_mode)
        self.display_mode_checkbutton.grid(row=3, column=0, columnspan=3, pady=10, sticky="w")

        self.start_button = tk.Button(root, text="Start Flashing", command=self.flash_words)
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)

        self.display_window = None  # Initialize the display window as None

    def update_slider(self, event):
        # Limit the value to 2 decimal places
        self.time_value.set(f"{float(self.time_value.get()):.2f}")

    def toggle_display_mode(self):
        if self.display_mode_var.get() == 0:
            display_bg = "white"
            label_fg = "black"
            label_bg = "white"
        else:
            display_bg = "black"
            label_fg = "white"
            label_bg = "black"

        if self.display_window is not None:
            self.display_window.destroy()  # Destroy the existing display window

        self.display_window = tk.Toplevel(self.root)  # Recreate the display window
        self.display_window.configure(bg=display_bg)
        self.display_label = tk.Label(self.display_window, text="", font=("Arial", 24), fg=label_fg, bg=label_bg)
        self.display_label.pack(padx=20, pady=20)
        self.display_window.resizable(True, True)  # Enable resizing
        self.display_window.withdraw()

    def flash_words(self):
        self.toggle_display_mode()  # Apply display mode

        text = self.text_entry.get()
        time_duration = float(self.time_value.get())
        font_size = int(self.font_size_value.get())

        words = text.split()
        self.display_window.deiconify()  # Show the display window

        for word in words:
            self.display_label.config(text=word, font=("Arial", font_size))
            self.root.update()
            self.root.after(int(time_duration * 1000))

        self.display_label.config(text="")  # Clear the text
        self.display_window.withdraw()  # Hide the display window

if __name__ == "__main__":
    root = tk.Tk()
    app = WordFlasherApp(root)
    root.mainloop()
