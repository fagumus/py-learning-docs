import tkinter as tk


def mile_to_km(val):
    return float(val) * 1.6


def cal_button_clicked():
    km_val = mile_to_km(miles_input.get())
    km_var.set(km_val)


window = tk.Tk()
window.title("Dönüştürücü: mil -> km")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)

miles_input = tk.Entry(width=15)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="mil")
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="eşittir")
is_equal_label.grid(column=0, row=1)

km_var = tk.DoubleVar()
km_label_result = tk.Label(text="", textvariable=km_var)
km_label_result.grid(column=1, row=1)

km_label = tk.Label(text="km")
km_label.grid(column=2, row=1)

calc_button = tk.Button(text="Hesapla", command=cal_button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()