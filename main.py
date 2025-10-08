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
        output_box.config(state='normal')
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
        output_box.config(state='disabled')
        feedback_label.config(text="")

def copy_text():
    """Copies the content of the output text box to the clipboard."""
    output_text = output_box.get("1.0", tk.END).strip()
    if output_text:
        root.clipboard_clear()
        root.clipboard_append(output_text)
        feedback_label.config(text="Copied! 🧽")
        root.after(2000, lambda: feedback_label.config(text=""))

def clear_text():
    """Clears the input and output text boxes and feedback label."""
    input_box.delete("1.0", tk.END)
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.config(state='disabled')
    feedback_label.config(text="")

# Set up the Tkinter window
root = tk.Tk()
root.title("🧽 SpongeMemeTextConverter")
root.geometry("450x350")
root.minsize(400, 300)
root.configure(bg="#87CEEB")  # Sky blue for Bikini Bottom

# Apply SpongeBob-themed styles
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=("Comic Sans MS", 12, "bold"), padding=10, background="#FFD700")
style.configure("TLabel", font=("Comic Sans MS", 14, "bold"), background="#87CEEB")
style.map("TButton", background=[('active', '#32CD32')])  # Lime green on click

# Main frame for centered content
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Input label and text box
input_label = ttk.Label(main_frame, text="Enter Text:")
input_label.pack(pady=(0, 5))
input_box = tk.Text(main_frame, height=3, width=40, font=("Comic Sans MS", 12), wrap="word")
input_box.pack(pady=(0, 10))

# Convert and Clear buttons side by side
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)
convert_button = ttk.Button(button_frame, text="Convert", command=convert_text)
convert_button.pack(side="left", padx=5)
clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side="left", padx=5)

# Output label and read-only text box
output_label = ttk.Label(main_frame, text="Text Output:")
output_label.pack(pady=(10, 5))
output_box = tk.Text(main_frame, height=3, width=40, font=("Comic Sans MS", 12), wrap="word", state='disabled')
output_box.pack(pady=(0, 10))

# Copy button
copy_button = ttk.Button(main_frame, text="Copy", command=copy_text)
copy_button.pack(pady=5)

# Feedback label for copy confirmation
feedback_label = ttk.Label(main_frame, text="", font=("Comic Sans MS", 10), foreground="#228B22")
feedback_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()