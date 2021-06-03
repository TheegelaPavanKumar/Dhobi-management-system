from tkinter import *
import sqlite3

root=Tk()
root.geometry('1000x700')
root.title("Dhobi Management System")
root.configure(background="powder blue")

text1=StringVar()
text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()
text6=StringVar()
text7=StringVar()
text8=StringVar()
text9=StringVar()
text10=StringVar()
text11=StringVar()
text12=StringVar()
text13=StringVar()


db = sqlite3.connect('storage.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clothes(enroll TEXT, date TEXT, shirt TEXT, pant TEXT, lower TEXT, short TEXT, tshirt TEXT, bedsheet TEXT, pillowcover TEXT, towel TEXT, dupatta TEXT, kurta TEXT, pajama TEXT)")
db.commit()

lab=Label(root,text='Enroll:',font=('none 13 bold'))
lab.place(x=0,y=80)

entenroll=Entry(root,width=20,font=('none 13 bold'),textvar=text1)
entenroll.place(x=80,y=80)

entdate=Entry(root,width=20,font=('none 13 bold'),textvar=text2)
entdate.place(x=400,y=80)

lab1=Label(root,text='Date:',font=('none 13 bold'))
lab1.place(x=300,y=80)


lab2=Label(root,text='Shirt:',font=('none 13 bold'))
lab2.place(x=0,y=120)

entshirt=Entry(root,width=20,font=('none 13 bold'),textvar=text3)
entshirt.place(x=80,y=120)

entpant=Entry(root,width=20,font=('none 13 bold'),textvar=text4)
entpant.place(x=400,y=120)

lab3=Label(root,text='Pant:',font=('none 13 bold'))
lab3.place(x=300,y=120)


lab4=Label(root,text='Lower:',font=('none 13 bold'))
lab4.place(x=0,y=160)

entlower=Entry(root,width=20,font=('none 13 bold'),textvar=text5)
entlower.place(x=80,y=160)

entshort=Entry(root,width=20,font=('none 13 bold'),textvar=text6)
entshort.place(x=400,y=160)

lab5=Label(root,text='Short:',font=('none 13 bold'))
lab5.place(x=300,y=160)


lab6=Label(root,text='Tshirt:',font=('none 13 bold'))
lab6.place(x=0,y=200)

enttshirts=Entry(root,width=20,font=('none 13 bold'),textvar=text7)
enttshirts.place(x=80,y=200)

entbedsheet=Entry(root,width=20,font=('none 13 bold'),textvar=text8)
entbedsheet.place(x=400,y=200)

lab7=Label(root,text='Bedsheet:',font=('none 13 bold'))
lab7.place(x=300,y=200)

lab8=Label(root,text='Pillowcover:',font=('none 13 bold'))
lab8.place(x=600,y=160)

entpillowcover=Entry(root,width=20,font=('none 13 bold'),textvar=text9)
entpillowcover.place(x=700,y=160)

enttowel=Entry(root,width=20,font=('none 13 bold'),textvar=text10)
enttowel.place(x=700,y=120)

lab9=Label(root,text='Towel:',font=('none 13 bold'))
lab9.place(x=600,y=120)


lab10=Label(root,text='Dupatta:',font=('none 13 bold'))
lab10.place(x=300,y=240)

entdupatta=Entry(root,width=20,font=('none 13 bold'),textvar=text11)
entdupatta.place(x=400,y=240)

entkurta=Entry(root,width=20,font=('none 13 bold'),textvar=text12)
entkurta.place(x=80,y=240)

lab11=Label(root,text='Kurta:',font=('none 13 bold'))
lab11.place(x=0,y=240)


lab12=Label(root,text='Pajama:',font=('none 13 bold'))
lab12.place(x=600,y=200)

entpajama=Entry(root,width=20,font=('none 13 bold'),textvar=text13)
entpajama.place(x=700,y=200)




def insert():
   
   enroll1 = text1.get()
   date1 = text2.get()
   shirt1 = text3.get()
   pant1 = text4.get()
   lower1 = text5.get()
   short1 = text6.get()
   tshirt1 = text7.get()
   bedsheet1 = text8.get()
   pillowcover1 = text9.get()
   towel1 = text10.get()
   dupatta1 = text11.get()
   kurta1 = text12.get()
   pajama1 = text13.get()
   conn = sqlite3.connect('storage.db')
   with conn:
      cursor = conn.cursor()
      cursor.execute('INSERT INTO clothes(enroll, date, shirt, pant, lower, short, tshirt, bedsheet, pillowcover, towel, dupatta, kurta, pajama) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(enroll1, date1, shirt1, pant1, lower1, short1, tshirt1, bedsheet1, pillowcover1, towel1, dupatta1, kurta1, pajama1,))
      db.close()
   

def show():
   connt = sqlite3.connect('storage.db')
   cursor = connt.cursor()
   cursor.execute('SELECT * FROM clothes')
   for row in cursor.fetchall():
      print(row)




enroll=StringVar()
date=StringVar()
shirt=StringVar()
pant=StringVar()
lower=StringVar()
short=StringVar()
tshirt=StringVar()
bedsheet=StringVar()
pillowcover=StringVar()
towel=StringVar()
dupatta=StringVar()
kurta=StringVar()
pajama=StringVar() 
def update():
   enr=enroll.get()
   dt=date.get()
   shit=shirt.get()
   pnt=pant.get()
   lwr=lower.get()
   shot=short.get()
   tshit=tshirt.get()
   bdsht=bedsheet.get()
   pilcvr=pillowcover.get()
   twl=towel.get()
   dupt=dupatta.get()
   kta=kurta.get()
   pjm=pajama.get()
   
   connnt=sqlite3.connect('storage.db')
   cursor = connnt.cursor()
   cursor.execute("UPDATE clothes SET date = ?, shirt = ?, pant = ?, lower = ?, short = ?, tshirt = ?, bedsheet = ?,pillowcover = ?, towel = ?, dupatta = ?, kurta = ?, pajama = ?  WHERE enroll = ?",(dt,shit,pnt,lwr,shot,tshit,bdsht,pilcvr,twl,dupt,kta,pjm,enr))
   connnt.commit()

dell=StringVar()
def dele():
   dee=dell.get()
   connnt=sqlite3.connect('storage.db')
   cursor = connnt.cursor()
   cursor.execute("DELETE FROM clothes WHERE enroll = ?",(dee,))
   connnt.commit()
   
labheading=Label(root,text='Dhobi Management :',font=('none 19 bold'),bg='red')
labheading.place(x=350,y=0)   

butupdate=Button(root,padx=2,pady=2,text='Update',command=update,font=('none 13 bold'),relief='raise')
butupdate.place(x=80,y=520)
      
labuenroll=Label(root,text='Enroll :',font=('none 13 bold'))
labuenroll.place(x=0,y=320)

enttupadteenroll=Entry(root,width=20,font=('none 13 bold'),textvar=enroll)
enttupadteenroll.place(x=80,y=320)

labudate=Label(root,text='Date :',font=('none 13 bold'))
labudate.place(x=300,y=320)

enttupadtedate=Entry(root,width=20,font=('none 13 bold'),textvar=date)
enttupadtedate.place(x=400,y=320)

labushirt=Label(root,text='Shirt :',font=('none 13 bold'))
labushirt.place(x=0,y=360)

entupdateshirt=Entry(root,width=20,font=('none 13 bold'),textvar=shirt)
entupdateshirt.place(x=80,y=360)

labupant=Label(root,text='Pant :',font=('none 13 bold'))
labupant.place(x=300,y=360)

entupdatepant=Entry(root,width=20,font=('none 13 bold'),textvar=pant)
entupdatepant.place(x=400,y=360)

labulower=Label(root,text='Lower :',font=('none 13 bold'))
labulower.place(x=0,y=400)

entupdatelower=Entry(root,width=20,font=('none 13 bold'),textvar=lower)
entupdatelower.place(x=80,y=400)

labushort=Label(root,text='Short :',font=('none 13 bold'))
labushort.place(x=300,y=400)

entupdateshort=Entry(root,width=20,font=('none 13 bold'),textvar=short)
entupdateshort.place(x=400,y=400)

labutshirt=Label(root,text='Tshirt :',font=('none 13 bold'))
labutshirt.place(x=0,y=440)

entupdatetshirt=Entry(root,width=20,font=('none 13 bold'),textvar=tshirt)
entupdatetshirt.place(x=80,y=440)

labubedsheet=Label(root,text='Bedsheet :',font=('none 13 bold'))
labubedsheet.place(x=300,y=440)

entupdatebedsheet=Entry(root,width=20,font=('none 13 bold'),textvar=bedsheet)
entupdatebedsheet.place(x=400,y=440)

labupillowcover=Label(root,text='Pillowcover :',font=('none 13 bold'))
labupillowcover.place(x=600,y=400)

entupdatepillowcover=Entry(root,width=20,font=('none 13 bold'),textvar=pillowcover)
entupdatepillowcover.place(x=700,y=400)

labutowel=Label(root,text='Towel :',font=('none 13 bold'))
labutowel.place(x=600,y=360)

entupdatetowel=Entry(root,width=20,font=('none 13 bold'),textvar=towel)
entupdatetowel.place(x=700,y=360)

labudupatta=Label(root,text='Dupatta :',font=('none 13 bold'))
labudupatta.place(x=300,y=480)

entupdatedupatta=Entry(root,width=20,font=('none 13 bold'),textvar=dupatta)
entupdatedupatta.place(x=400,y=480)

labukurta=Label(root,text='Kurta :',font=('none 13 bold'))
labukurta.place(x=0,y=480)

entupdatekurta=Entry(root,width=20,font=('none 13 bold'),textvar=kurta)
entupdatekurta.place(x=80,y=480)

labupajama=Label(root,text='Pajama :',font=('none 13 bold'))
labupajama.place(x=600,y=440)

entupdatepajama=Entry(root,width=20,font=('none 13 bold'),textvar=pajama)
entupdatepajama.place(x=700,y=440)

labdelete=Label(root,text='Delete :',font=('none 13 bold'))
labdelete.place(x=0,y=560)

endelete=Entry(root,width=20,textvar=dell,font=('none 13 bold'))
endelete.place(x=90,y=560)


butdel=Button(root,padx=2,pady=2,text='Delete',command=dele,font=('none 13 bold'))
butdel.place(x=90,y=600)
    

but=Button(root,padx=2,pady=2,text='Submit',command=insert,font=('none 13 bold'))
but.place(x=60,y=280)

res=Button(root,padx=2,pady=2,text='Show',command=show,font=('none 13 bold'))
res.place(x=160,y=280)



root.mainloop()
