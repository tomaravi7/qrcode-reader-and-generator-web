from typing import Sized
import png
from pyqrcode import QRCode
import subprocess
import pyqrcode
from tkinter import *

window = Tk()

window.title("QR-Code generator")
# photo = PhotoImage(file = "D:\AVI PC BACK UP 24-06-2021\PROJECTS\PYTHON\qr.png")
# window.iconphoto(False, photo)
window.geometry("500x200")
window.configure(bg = "darkgrey")

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Options', menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

Label(text = "Enter your link below",font="arial",width=25,borderwidth=0).grid(row=1,column=0)
link=Entry(window,width=40)
link.grid(column=0,row=2)
Button(text = "Create qr code",font="arial",width=25, bg = "grey", fg = "white",activebackground="white",activeforeground="Black",borderwidth=0).grid(row=4,column=0)

window.mainloop()

link=input("Please enter the link to want to get the qr code of : ")
url=pyqrcode.create(link)
url.png("qr.png",scale=8)
subprocess.Popen('explorer "./"')
