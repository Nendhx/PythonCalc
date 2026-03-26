import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("Calculator")
root.minsize(400, 500)
root.geometry("400x500")
root.grid()
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

#variables
formstr = tk.StringVar()
ansstr = tk.StringVar(value="0")

#functions
def add_func(a, b):
    return a + b

def subtract_func(a, b):
    return a - b

def multiply_func(a, b):
    return a * b

def divide_func(a, b):
    if(b == 0):
        return "Error"
    return a / b

def clear():
    ansstr.set('0')

def num_press(value):
    ansstr.set(ansstr.get() + str(value))


#styles
style = ttk.Style(root)
style.theme_use("default")
style.configure("math.TButton", background="#ff9500", foreground="white", font=("Helvetica", 12, "bold"))
style.map("math.TButton", background=[("hover", "#ffa500")])
style.configure("operator.TButton", background="#636267", foreground="white", font=("Helvetica", 12, "bold"))
style.map("operator.TButton", background=[("hover", "#8f8e94")])
style.configure("number.TButton", background="#3a3a3c", foreground="white", font=("Helvetica", 12, "bold"))
style.map("number.TButton", background=[("hover", "#48484a")])
style.configure("label.TLabel", background="black", foreground="white", padding=(10, 20))

#buttons
formula = ttk.Label(root, textvariable=formstr, anchor='e', style="label.TLabel", font=("Helvetica", 16, "bold")).grid(column=0, row=0, columnspan=4, sticky="nsew")
answer = ttk.Label(root, textvariable=ansstr, anchor='e', style="label.TLabel", font=("Helvetica", 20, "bold")).grid(column=0, row=1, columnspan=4, sticky="nsew")

button_clear = ttk.Button(root, text="AC", style="operator.TButton", command=clear).grid(column=0, row=2, sticky="nsew")
button_invert = ttk.Button(root, text="+/-", style="operator.TButton").grid(column=1, row=2, sticky="nsew")
button_remainder = ttk.Button(root, text="%", style="operator.TButton").grid(column=2, row=2, sticky="nsew")
button_divide = ttk.Button(root, text="/", style="math.TButton").grid(column=3, row=2, sticky="nsew")

button7 = ttk.Button(root, text="7", style="number.TButton", command=lambda: num_press(7)).grid(column=0, row=3, sticky="nsew")
button8 = ttk.Button(root, text="8", style="number.TButton", command=lambda: num_press(8)).grid(column=1, row=3, sticky="nsew")
button9 = ttk.Button(root, text="9", style="number.TButton", command=lambda: num_press(9)).grid(column=2, row=3, sticky="nsew")
button_multiply = ttk.Button(root, text="*", style="math.TButton").grid(column=3, row=3, sticky="nsew")

button4 = ttk.Button(root, text="4", style="number.TButton", command=lambda: num_press(4)).grid(column=0, row=4, sticky="nsew")
button5 = ttk.Button(root, text="5", style="number.TButton", command=lambda: num_press(5)).grid(column=1, row=4, sticky="nsew")
button6 = ttk.Button(root, text="6", style="number.TButton", command=lambda: num_press(6)).grid(column=2, row=4, sticky="nsew")
button_minus = ttk.Button(root, text="-", style="math.TButton").grid(column=3, row=4, sticky="nsew")

button1 = ttk.Button(root, text="1", style="number.TButton", command=lambda: num_press(1)).grid(column=0, row=5, sticky="nsew")
button2 = ttk.Button(root, text="2", style="number.TButton", command=lambda: num_press(2)).grid(column=1, row=5, sticky="nsew")
button3 = ttk.Button(root, text="3", style="number.TButton", command=lambda: num_press(3)).grid(column=2, row=5, sticky="nsew")
button_plus = ttk.Button(root, text="+", style="math.TButton").grid(column=3, row=5, sticky="nsew")

button0 = ttk.Button(root, text="0", style="number.TButton", command=lambda: num_press(0)).grid(column=0, row=6, columnspan=2, sticky="nsew")
button_dot = ttk.Button(root, text=".", style="number.TButton").grid(column=2, row=6, sticky="nsew")
button_equal = ttk.Button(root, text="=", style="math.TButton").grid(column=3, row=6, sticky="nsew")

root.mainloop()