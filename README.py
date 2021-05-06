from tkinter import*
def aboba ():
    global a
    if a==0:
        lab['text']=question3[0]
        rb1['text']=answer3[0]
        rb2['text']=answer3[1]
        rb3['text']=answer3[2]
        rb4['text']=answer3[3]
    if a==1:
        lab['text']=question3[1]
        rb1['text']=answer3[4]
        rb2['text']=answer3[5]
        rb3['text']=answer3[6]
        rb4['text']=answer3[7]
    if a==2:
        lab['text']=question3[2]
        rb1['text']=answer3[8]
        rb2['text']=answer3[9]
        rb3['text']=answer3[10]
        rb4['text']=answer3[11]
    if a==3:
        lab['text']=question3[3]
        rb1['text']=answer3[12]
        rb2['text']=answer3[13]
        rb3['text']=answer3[14]
        rb4['text']=answer3[15]
    a+=1
a=0
question1=[]
answer1=[]
with open('Вахтерша.txt','r',encoding='utf-8') as f1:
    s=f1.readlines()
    question1.append(s[0])
    answer1.append(s[1])
    question2=[]
with open('Физрук.txt','r',encoding='utf-8') as f2:
    s=f2.readlines()
    question2.append(s[0])
    question2.append(s[1])
    question2.append(s[2])
    question3=[]
    answer3=[]
with open('ОБЖ.txt','r',encoding='utf-8') as f3:
    s=f3.readlines()
    question3.append(s[0])
    answer3.append(s[1])
    answer3.append(s[2])
    answer3.append(s[3])
    answer3.append(s[4])
    question3.append(s[5])
    answer3.append(s[6])
    answer3.append(s[7])
    answer3.append(s[8])
    answer3.append(s[9])
    question3.append(s[10])
    answer3.append(s[11])
    answer3.append(s[12])
    answer3.append(s[13])
    answer3.append(s[14])
    question3.append(s[15])
    answer3.append(s[16])
    answer3.append(s[17])
    answer3.append(s[18])
    answer3.append(s[19])
    question4=[]
    answer4=[]
with open('Физичка.txt','r',encoding='utf-8') as f4:
    s=f4.readlines()
    question4.append(s[0])
    answer4.append(s[1])
    answer4.append(s[2])
    answer4.append(s[3])
    answer4.append(s[4])
    question4.append(s[5])
    answer4.append(s[6])
    answer4.append(s[7])
    answer4.append(s[8])
    answer4.append(s[9])
    question4.append(s[10])
    answer4.append(s[11])
    answer4.append(s[12])
    answer4.append(s[13])
    answer4.append(s[14])
    question4.append(s[15])
    answer4.append(s[16])
    answer4.append(s[17])
    answer4.append(s[18])
    answer4.append(s[19])
    question4.append(s[20])
    answer4.append(s[21])
    question4.append(s[22])
    answer4.append(s[23])
    question4.append(s[24])
    answer4.append(s[25])
    question4.append(s[26])
    answer4.append(s[27])
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
but=Button(root,text='Ответить',height=3,width=15,command=aboba)
but.place(x=880,y=640)
root.mainloop()

