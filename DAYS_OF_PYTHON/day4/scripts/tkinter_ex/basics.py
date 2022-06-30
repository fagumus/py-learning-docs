import tkinter as tk

window = tk.Tk()
window.title("Tkinter GUI Temelleri")
window.minsize(width=300, height=200)

### Bileşenler

# 1. label
my_label = tk.Label(text="Etiket yazısı.", font=("Arial", 20, "bold"))
my_label.pack() # default olarak my_label bileşenini pencereye üste, ortalı olarak yerleştirir. Ör: sol için pack(side="left")

my_label["text"] = "Değiştirilen metin."

my_label.config(text = "Değiştirilen yeni metin.")

# 2. button
def my_button_clicked():
    # my_label["text"] = "my_button_clicked tamam!"
    my_label["text"] = my_entry.get() # get the text

my_button = tk.Button(text="Tıkla!", command=my_button_clicked)
my_button.pack()

# 3. entry: girdi alır
my_entry = tk.Entry(width=25)
my_entry.pack()




# Pencere gelen eventleri dinleme halinde ve açık olsun
# mainloop() her zaman son satırda olmalı
window.mainloop()

