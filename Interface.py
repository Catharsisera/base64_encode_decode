import tkinter as Tr
from Base64 import Base64, BASE64
from tkinter.ttk import Combobox, Radiobutton
from tkinter import filedialog

ch_file = ""

def openf(event):
    global ch_file
    file = filedialog.askopenfilename()
    ch_file = file

def fmodify(event):
    name = ch_file[ch_file.rfind("/") + 1:]
    file = open(ch_file, 'rb')
    btss = file.read()
    file.close()
    encoding = 'utf-8'
    if selected.get() == 0:
        newname = name + "." + "BASE64"
        newbtss = bytes(Base64.encode(BASE64, btss), encoding)
    elif selected.get() == 1:
        newname = name + "_decoded"
        print(newname)
        newbtss = Base64.decode(BASE64, btss.decode(encoding), encoding)
    file = open(newname, 'wb')
    file.write(bytes(newbtss))
    file.close()

window = Tr.Tk()
window.title('Программа для кодирования файлов')
window.geometry('320x150')

lblr = Tr.Label(window, text="Кодировка:")
lblr.grid(column=1, row=0, columnspan=2)

selected= Tr.IntVar()

rad1 = Radiobutton(window, text='Кодирование', width=20, value=0, variable=selected)
rad1.grid(column=2, row=2)
rad1 = Radiobutton(window, text='Декодирование', width=20, value=1, variable=selected)
rad1.grid(column=2, row=3)

btn2 = Tr.Button(window, text="Открыть файл", height=7, width=20)
btn2.bind("<Button-1>", openf)
btn2.grid(column=0, row=0, rowspan=6, pady=2, padx=2)

btn3 = Tr.Button(window, text="Обработать файл")
btn3.bind("<Button-1>", fmodify)
btn3.grid(column=1, row=5, columnspan=2)

window.mainloop()