from tkinter import*
from tkinter.ttk import Combobox

window=Tk()
window.title('Welcome to Python')

w=600
h=500
ws=window.winfo_screenwidth()
hs=window.winfo_screenheight()
x=(ws-w)/2
y=(hs-h)/2
window.geometry("%dx%d+%d+%d"%(w,h,x,y))
window.configure(background='#300000')

lbl=Label(window, text="This is my First Window", bg='yellow', fg='red', font=("Times New Roman", 16))
lbl.place(x=60, y=50)

txtfld=Entry(window, text="Enter the text", show='*', bd=5)
txtfld.place(x=80, y=150)

btn=Button(window, text="Click the Button", fg='blue')
btn.place(x=80, y=100)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=300,y=150)
r2.place(x=350, y=150)

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=360, y=200)
C2.place(x=360, y=250)

var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=80, y=180)

window.mainloop()
