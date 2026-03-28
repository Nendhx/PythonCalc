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
def format_float_str(num):
    result = f'{num:g}'
    return result

def clear():
    formstr.set('')
    ansstr.set('0')

def invert():
    math_press("invert")

def num_press(value):
    if(formstr.get() == ''):
        pass
    elif(formstr.get()[-1] == '='):
        formstr.set('')
        ansstr.set('0')
    curr_val = ansstr.get()
    if(len(curr_val) > 18):
        return
    if(curr_val == '0' or curr_val == '-0' or curr_val == "Error"):
        ansstr.set(value)
    else:
        ansstr.set(curr_val + str(value))

def decimal():
    if(formstr.get() == ''):
        pass
    elif(formstr.get()[-1] == '='):
        formstr.set('')
        ansstr.set('0')
    curr_val = ansstr.get()
    if('.' not in curr_val):
        ansstr.set(curr_val + '.')

def math_func(a, b, operator):
    if(operator == '+'):
        return a + b
    elif(operator == '-'):
        return a - b
    elif(operator == '*'):
        return a * b
    elif(operator == '/'):
        if(b == 0):
            return "Error"
        return a / b
    elif(operator == '%'):
        if(b == 0):
            return "Error"
        return a % b
    
def math_press(operator):
    prev_str = formstr.get()
    curr_value = float(ansstr.get())
    prev_value = 0
    answer = curr_value
    if(prev_str != ''):
        prev_operator = prev_str[-1]
        if(prev_operator != '='):
            prev_value = float(prev_str[0:-2])
            answer = math_func(prev_value, curr_value, prev_operator)
    if(answer == "Error"):
        formstr.set('')
        ansstr.set(answer)
        return
    if(operator == "invert"):
        formstr.set('')
        ansstr.set(format_float_str(float(answer) * -1))
        return
    formstr.set(f"{format_float_str(float(answer))} {operator}")
    ansstr.set('0')

def equal_press():
    prev_str = formstr.get()
    curr_value = float(ansstr.get())
    prev_value = 0
    answer = curr_value
    if(prev_str != ''):
        prev_operator = prev_str[-1]
        prev_value = float(prev_str[0:-2])
        answer = math_func(prev_value, curr_value, prev_operator)
    else:
        formstr.set(f"{format_float_str(curr_value)} =")
        ansstr.set(format_float_str(float(answer)))
        return
    if(answer == "Error"):
        formstr.set('')
        ansstr.set(answer)
        return
    formstr.set(f"{format_float_str(prev_value)} {prev_operator} {format_float_str(curr_value)} =")
    ansstr.set(format_float_str(float(answer)))

#styles
style = ttk.Style(root)
style.theme_use("default")
style.configure("math.TButton", background="#ff9500", foreground="white", font=("Helvetica", 12, "bold"))
style.map("math.TButton", background=[("hover", "#ffa500")])
style.configure("operator.TButton", background="#636267", foreground="white", font=("Helvetica", 12, "bold"))
style.map("operator.TButton", background=[("hover", "#8f8e94")])
style.configure("number.TButton", background="#3a3a3c", foreground="white", font=("Helvetica", 12, "bold"))
style.map("number.TButton", background=[("hover", "#48484a")])
style.configure("label.TLabel", background="black", foreground="white", padding=(10, 0))

#buttons
formula = ttk.Label(root, textvariable=formstr, anchor='se', style="label.TLabel", font=("Helvetica", 12, "bold")).grid(column=0, row=0, columnspan=4, sticky="nsew")
answer = ttk.Label(root, textvariable=ansstr, anchor='e', style="label.TLabel", font=("Helvetica", 20, "bold")).grid(column=0, row=1, columnspan=4, sticky="nsew")

button_clear = ttk.Button(root, text="AC", style="operator.TButton", command=clear).grid(column=0, row=2, sticky="nsew")
button_invert = ttk.Button(root, text="+/-", style="operator.TButton", command=invert).grid(column=1, row=2, sticky="nsew")
button_remainder = ttk.Button(root, text="%", style="operator.TButton", command=lambda: math_press("%")).grid(column=2, row=2, sticky="nsew")
button_divide = ttk.Button(root, text="/", style="math.TButton", command=lambda: math_press("/")).grid(column=3, row=2, sticky="nsew")

button7 = ttk.Button(root, text="7", style="number.TButton", command=lambda: num_press(7)).grid(column=0, row=3, sticky="nsew")
button8 = ttk.Button(root, text="8", style="number.TButton", command=lambda: num_press(8)).grid(column=1, row=3, sticky="nsew")
button9 = ttk.Button(root, text="9", style="number.TButton", command=lambda: num_press(9)).grid(column=2, row=3, sticky="nsew")
button_multiply = ttk.Button(root, text="*", style="math.TButton", command=lambda: math_press("*")).grid(column=3, row=3, sticky="nsew")

button4 = ttk.Button(root, text="4", style="number.TButton", command=lambda: num_press(4)).grid(column=0, row=4, sticky="nsew")
button5 = ttk.Button(root, text="5", style="number.TButton", command=lambda: num_press(5)).grid(column=1, row=4, sticky="nsew")
button6 = ttk.Button(root, text="6", style="number.TButton", command=lambda: num_press(6)).grid(column=2, row=4, sticky="nsew")
button_minus = ttk.Button(root, text="-", style="math.TButton", command=lambda: math_press("-")).grid(column=3, row=4, sticky="nsew")

button1 = ttk.Button(root, text="1", style="number.TButton", command=lambda: num_press(1)).grid(column=0, row=5, sticky="nsew")
button2 = ttk.Button(root, text="2", style="number.TButton", command=lambda: num_press(2)).grid(column=1, row=5, sticky="nsew")
button3 = ttk.Button(root, text="3", style="number.TButton", command=lambda: num_press(3)).grid(column=2, row=5, sticky="nsew")
button_plus = ttk.Button(root, text="+", style="math.TButton", command=lambda: math_press("+")).grid(column=3, row=5, sticky="nsew")

button0 = ttk.Button(root, text="0", style="number.TButton", command=lambda: num_press(0)).grid(column=0, row=6, columnspan=2, sticky="nsew")
button_dot = ttk.Button(root, text=".", style="number.TButton", command=decimal).grid(column=2, row=6, sticky="nsew")
button_equal = ttk.Button(root, text="=", style="math.TButton", command=equal_press).grid(column=3, row=6, sticky="nsew")

root.mainloop()
