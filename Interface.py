from Base64 import Base64, BASE64
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Base64')
window.geometry('350x200-600-400')

def openFile():
    global pathToFile
    pathToFile = filedialog.askopenfilename()

def modifyFile():
    fileName = pathToFile[pathToFile.rfind("/") + 1:]
    file = open(pathToFile, 'rb')
    sequenceBytes = file.read()
    file.close()
    encoding = 'utf-8'
    if selected.get() == 0:
        newFileName = fileName + "." + "BASE64"
        newSequenceBytes = bytes(Base64.encode(BASE64, sequenceBytes), encoding)
    elif selected.get() == 1:
        newFileName = fileName + "_decoded"
        newSequenceBytes = Base64.decode(BASE64, sequenceBytes.decode(encoding), encoding)

    file = open(newFileName, 'wb')
    file.write(bytes(newSequenceBytes))
    file.close()

label1 = Label(master=window, text="Выбор действия:", font=('Times New Roman', 12),justify=CENTER, padx=10, pady=12)
label1.pack()

selected = IntVar()

radbutton = Radiobutton(master=window, text='Кодирование', font=('Times New Roman', 12), width=20, value=0, variable=selected)
radbutton.pack()
radbutton = Radiobutton(master=window, text='Декодирование', font=('Times New Roman', 12), width=20, value=1, variable=selected)
radbutton.pack()

frame1 = Frame(padx=10, pady=12)

button1 = Button(master=frame1, text="Открыть", font=('Times New Roman', 12), height=4, width=18, command=openFile)
button1.pack(side=LEFT)

button2 = Button(master=frame1, text="Изменить", font=('Times New Roman', 12), height=4, width=18, command=modifyFile)
button2.pack(side=RIGHT)

frame1.pack()

window.mainloop()