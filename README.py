from tkinter import*
root=Tk()
root.title('Школа')
root.geometry('1000x700')
root["bg"] ='#A9A9A9'
lab=Label(root, text='Здесь вопросы',height=5)
lab.place(x=0,y=0)
var=IntVar()
rb1=Radiobutton(root,text='1)',variable=var,value=1)
rb1.place(x=120,y=150)
rb2=Radiobutton(root,text='2)',variable=var,value=2)
rb2.place(x=120,y=200)
rb3=Radiobutton(root,text='3)',variable=var,value=3)
rb3.place(x=120,y=250)
rb4=Radiobutton(root,text='4)',variable=var,value=4)
rb4.place(x=120,y=300)
lab1=Label(root,text='Шкала очков (дневник или что там я хз)',height=3)
lab1.place(x=25,y=640)
but=Button(root,text='Ответить',height=3,width=15)
but.place(x=880,y=640)
root.mainloop()