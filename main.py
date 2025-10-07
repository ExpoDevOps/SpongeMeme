import random
import tkinter as tk
from tkinter import ttk

def to_mocking_text(text):
    """
    Converts input text to Mocking SpongeBob style by mostly alternating case,
    with some chance of consecutive same-case letters for irregularity.
    Preserves non-letter characters like spaces and punctuation.
    """
    result = []
    prev_upper = None
    for char in text:
        if char.isalpha():
            if prev_upper is None:
                is_upper = random.choice([True, False])
            else:
                if random.random() < 0.2:
                    is_upper = prev_upper
                else:
                    is_upper = not prev_upper
            result.append(char.upper() if is_upper else char.lower())
            prev_upper = is_upper
        else:
            result.append(char)
    return ''.join(result)

def convert_text():
    """Handles the button click to convert input text and display in output box."""
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        output = to_mocking_text(input_text)
        output_box.config(state='normal')  # Enable editing to update text
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state='disabled')  # Back to read-only

# Set up the Tkinter window
root = tk.Tk()
root.title("SpongeBob Mocking Text Converter")
root.geometry("400x300")

# Input label and text box
input_label = ttk.Label(root, text="Enter Text:")
input_label.pack(pady=5)
input_box = tk.Text(root, height=3, width=40)
input_box.pack(pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

# Output label and read-only text box
output_label = ttk.Label(root, text="Mocking Text Output:")
output_label.pack(pady=5)
output_box = tk.Text(root, height=3, width=40, state='disabled')
output_box.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()