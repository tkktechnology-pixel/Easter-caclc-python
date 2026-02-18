import tkinter as tk
from tkinter import font as tkfont

# Easter Calculator using the Meeus/Jones/Butcher algorithm
def easter_date(year: int) -> tuple[int, int]:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return month, day

def month_name(month: int) -> str:
    return "March" if month == 3 else "April" if month == 4 else f"Month {month}"

# --- GUI Logic ---
def calculate_easter():
    year_str = year_var.get().strip()

    # Validate: must be exactly 4 digits
    if not year_str.isdigit() or len(year_str) != 4:
        result_var.set("Please enter a valid 4-digit year.")
        result_label.config(fg="#c0392b")
        return

    year = int(year_str)
    month, day = easter_date(year)
    result_var.set(f"In {year}, Easter Sunday falls on\n{month_name(month)} {day}.")
    result_label.config(fg="#2c7a2c")

def clear_entry():
    year_var.set("")
    result_var.set("")
    year_entry.focus()

def only_digits(char):
    return char.isdigit()

# --- Build Window ---
root = tk.Tk()
root.title("Easter Date Calculator")
root.resizable(False, False)
root.configure(bg="#f5f0e8")

# Fonts
title_font  = tkfont.Font(family="Georgia", size=16, weight="bold")
label_font  = tkfont.Font(family="Helvetica", size=11)
entry_font  = tkfont.Font(family="Helvetica", size=13)
result_font = tkfont.Font(family="Georgia", size=13, weight="bold")
btn_font    = tkfont.Font(family="Helvetica", size=11)

PADDING = {"padx": 20, "pady": 10}

# Title
title_label = tk.Label(root, text="🐣  Easter Date Calculator",
                        font=title_font, bg="#f5f0e8", fg="#5b3a29")
title_label.pack(pady=(20, 5))

tk.Label(root, text="Using the Meeus/Jones/Butcher Algorithm",
         font=tkfont.Font(family="Helvetica", size=9, slant="italic"),
         bg="#f5f0e8", fg="#888").pack()

tk.Label(root, text="© 2026 TKK Technology",
         font=tkfont.Font(family="Helvetica", size=9, weight="bold"),
         bg="#f5f0e8", fg="#5b3a29").pack(pady=(2, 0))

tk.Frame(root, height=2, bg="#c8b89a").pack(fill="x", padx=20, pady=10)

# Year input
input_frame = tk.Frame(root, bg="#f5f0e8")
input_frame.pack(**PADDING)

tk.Label(input_frame, text="Enter a 4-Digit Year:", font=label_font,
         bg="#f5f0e8", fg="#3d2b1f").grid(row=0, column=0, sticky="w", padx=(0, 10))

year_var = tk.StringVar()

# Validation: allow only digits, max 4 characters
vcmd = root.register(lambda P: (P.isdigit() or P == "") and len(P) <= 4)
year_entry = tk.Entry(input_frame, textvariable=year_var, font=entry_font,
                      width=8, justify="center", bd=2, relief="groove",
                      validate="key", validatecommand=(vcmd, "%P"))
year_entry.grid(row=0, column=1)
year_entry.focus()

# Calculate button
calc_btn = tk.Button(root, text="Calculate Easter", font=btn_font,
                     bg="#8b5e3c", fg="white", activebackground="#6d4828",
                     activeforeground="white", relief="raised", bd=2,
                     padx=10, pady=5, cursor="hand2",
                     command=calculate_easter)
calc_btn.pack(pady=(5, 10))

# Bind Enter key
root.bind("<Return>", lambda e: calculate_easter())

# Result display
tk.Frame(root, height=2, bg="#c8b89a").pack(fill="x", padx=20)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=result_font,
                         bg="#f5f0e8", fg="#2c7a2c", justify="center",
                         wraplength=320)
result_label.pack(pady=15, padx=20)

tk.Frame(root, height=2, bg="#c8b89a").pack(fill="x", padx=20)

# Bottom buttons: Clear + Exit
btn_frame = tk.Frame(root, bg="#f5f0e8")
btn_frame.pack(pady=15)

clear_btn = tk.Button(btn_frame, text="Clear", font=btn_font,
                      bg="#d0a050", fg="white", activebackground="#b5893a",
                      activeforeground="white", relief="raised", bd=2,
                      width=10, pady=5, cursor="hand2",
                      command=clear_entry)
clear_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", font=btn_font,
                     bg="#8b2020", fg="white", activebackground="#6e1a1a",
                     activeforeground="white", relief="raised", bd=2,
                     width=10, pady=5, cursor="hand2",
                     command=root.destroy)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
