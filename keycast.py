from tkinter import *
from tkinter.scrolledtext import *
def onKeyPress(event):
    text.insert('end', 'pressed %s\n' % (event.char, ))
root = Tk()
root.geometry('300x200')
text = ScrolledText(root, background='black', foreground='white', font=('Consolas', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
