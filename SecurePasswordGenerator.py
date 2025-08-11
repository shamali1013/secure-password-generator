import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def score_and_label(password):
    length = len(password)
    score = 0

    if length < 6:
        length_score = 0
    elif length <= 8:
        length_score = 1
    elif length <= 12:
        length_score = 2
    else:
        length_score = 3
    score += length_score

    diversity = 0
    if any(c.islower() for c in password):
        diversity += 1
    if any(c.isupper() for c in password):
        diversity += 1
    if any(c.isdigit() for c in password):
        diversity += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password):
        diversity += 1
    score += diversity

    percent = int((score / 7) * 100)

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    elif score <= 6:
        label = "Strong"
    else:
        label = "Excellent"

    return percent, label


def generate_password_from_inputs(length, num_digits, num_lower, num_upper, num_special):
    if num_digits + num_lower + num_upper + num_special > length:
        raise ValueError("Sum of character counts cannot exceed total length.")

    digits = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password_chars = (
        [random.choice(digits) for _ in range(num_digits)] +
        [random.choice(lower) for _ in range(num_lower)] +
        [random.choice(upper) for _ in range(num_upper)] +
        [random.choice(special) for _ in range(num_special)]
    )

    remaining_length = length - len(password_chars)
    all_chars = digits + lower + upper + special
    password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

    random.shuffle(password_chars)
    return ''.join(password_chars)


def on_generate():
    try:
        length = int(var_length.get())
        nd = int(var_digits.get())
        nl = int(var_lower.get())
        nu = int(var_upper.get())
        ns = int(var_special.get())
    except Exception:
        messagebox.showerror("Invalid input", "Please enter valid integer values.")
        return

    try:
        pwd = generate_password_from_inputs(length, nd, nl, nu, ns)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    entry_result.config(state="normal")
    var_password.set(pwd)
    entry_result.config(state="readonly")

    pct, label = score_and_label(pwd)
    progress['value'] = pct

    if pct < 40:
        pb_style_name = "Red.Horizontal.TProgressbar"
        label_color = "#d9534f"
    elif pct < 70:
        pb_style_name = "Orange.Horizontal.TProgressbar"
        label_color = "#f0ad4e"
    else:
        pb_style_name = "Green.Horizontal.TProgressbar"
        label_color = "#28a745"

    progress.config(style=pb_style_name)
    label_strength.config(text=f"Strength: {label}", foreground=label_color)


def on_copy():
    pwd = var_password.get()
    if not pwd:
        messagebox.showinfo("Nothing to copy", "Generate a password first.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    btn_copy.config(text="Copied!")
    root.after(1200, lambda: btn_copy.config(text="Copy"))


def on_show_toggle():
    if var_show.get():
        entry_result.config(show="")
    else:
        entry_result.config(show="*")


def add_hover_effect(widget, normal_bg, hover_bg):
    def on_enter(e):
        widget['bg'] = hover_bg
    def on_leave(e):
        widget['bg'] = normal_bg
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)


root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("600x500")
root.minsize(400, 300)
root.resizable(True, True)

style = ttk.Style(root)
style.theme_use("clam")

style.configure("Green.Horizontal.TProgressbar", troughcolor="#e9ecef", background="#28a745")
style.configure("Orange.Horizontal.TProgressbar", troughcolor="#e9ecef", background="#f0ad4e")
style.configure("Red.Horizontal.TProgressbar", troughcolor="#e9ecef", background="#d9534f")

BG = "#f4f6f8"
CARD = "#ffffff"
ACCENT = "#0d9488"
BTN_HOVER = "#0ba48f"
FONT_HEADER = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 10)
FONT_MONO = ("Consolas", 12, "bold")

root.configure(bg=BG)

card = tk.Frame(root, bg=CARD, bd=0, highlightthickness=0)
card.pack(padx=20, pady=20, fill="both", expand=True)

title = tk.Label(card, text="🔐 Secure Password Generator", font=FONT_HEADER, bg=CARD, fg="#111827")
title.pack(pady=(18, 6))

inp_frame = tk.Frame(card, bg=CARD)
inp_frame.pack(padx=20, pady=6, fill="x")

var_length = tk.StringVar(value="12")
var_digits = tk.StringVar(value="2")
var_lower = tk.StringVar(value="4")
var_upper = tk.StringVar(value="4")
var_special = tk.StringVar(value="2")

def labeled_entry(parent, text, textvar, row, col):
    lbl = ttk.Label(parent, text=text + ":", font=FONT_LABEL)
    lbl.grid(row=row, column=col*2, sticky="w", padx=(0,10), pady=8)
    ent = ttk.Entry(parent, textvariable=textvar, width=10)
    ent.grid(row=row, column=col*2 + 1, sticky="w", pady=8)
    return ent

l1 = labeled_entry(inp_frame, "Total length", var_length, 0, 0)
l2 = labeled_entry(inp_frame, "Digits", var_digits, 0, 1)
l3 = labeled_entry(inp_frame, "Lowercase", var_lower, 1, 0)
l4 = labeled_entry(inp_frame, "Uppercase", var_upper, 1, 1)
l5 = labeled_entry(inp_frame, "Special", var_special, 2, 0)

btn_frame = tk.Frame(card, bg=CARD)
btn_frame.pack(pady=(8, 10), fill="x")

btn_generate = tk.Button(btn_frame, text="Generate Password", font=("Segoe UI", 11, "bold"),
                         bg=ACCENT, fg="white", activebackground=BTN_HOVER,
                         relief="flat", padx=14, pady=8, command=on_generate)
btn_generate.grid(row=0, column=0, padx=(0,10))
add_hover_effect(btn_generate, ACCENT, BTN_HOVER)

btn_copy = tk.Button(btn_frame, text="Copy", font=("Segoe UI", 11), bg="#2563eb", fg="white",
                     activebackground="#1f4fd4", relief="flat", padx=12, pady=8, command=on_copy)
btn_copy.grid(row=0, column=1)
add_hover_effect(btn_copy, "#2563eb", "#1f4fd4")

out_frame = tk.Frame(card, bg=CARD)
out_frame.pack(padx=20, pady=(8,16), fill="x")

label_out = ttk.Label(out_frame, text="Generated password", font=FONT_LABEL)
label_out.grid(row=0, column=0, sticky="w")

var_password = tk.StringVar()
entry_result = ttk.Entry(out_frame, textvariable=var_password, font=FONT_MONO, width=40, state="readonly")
entry_result.grid(row=1, column=0, sticky="ew", pady=(8,0))

var_show = tk.BooleanVar(value=True)
chk_show = ttk.Checkbutton(out_frame, text="Show password", command=on_show_toggle, variable=var_show)
chk_show.grid(row=1, column=1, padx=(10,0))

strength_frame = tk.Frame(card, bg=CARD)
strength_frame.pack(padx=20, pady=(6,0), fill="x")

progress = ttk.Progressbar(strength_frame, orient="horizontal", length=400, mode="determinate", maximum=100)
progress.grid(row=0, column=0, sticky="ew")

label_strength = ttk.Label(strength_frame, text="Strength: ", font=FONT_LABEL)
label_strength.grid(row=0, column=1, padx=(10,0), sticky="w")

hint = ttk.Label(card, text="Tip: Ensure the sum of counts ≤ total length. Press Generate first.", font=("Segoe UI", 9), foreground="#6b7280")
hint.pack(side="bottom", pady=(10,12))

if not var_show.get():
    entry_result.config(show="*")

inp_frame.columnconfigure((1, 3), weight=1)
out_frame.columnconfigure(0, weight=1)
strength_frame.columnconfigure(0, weight=1)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("\nApplication closed by user.")
    try:
        root.destroy()
    except tk.TclError:
        pass

