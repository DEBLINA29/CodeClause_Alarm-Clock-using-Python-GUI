# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:47:01 2023

@author: debli
"""

from lib2to3.pgen2.token import LBRACE
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import *

window=Tk()
window.title("Alarm")
window.geometry("350x150")
window.configure(bg="black")



#frameline
frame_line=Frame(window,width=400,height=3,bg="black")
frame_line.grid(row=0,column=0)

#framebody
frame_body=Frame(window,width=400,height=290,bg="#AC7088")
frame_body.grid(row=1,column=0)

#load image
img=Image.open('i.png')
img.resize((100,100))
img=ImageTk.PhotoImage(img)

#place image
app_image= Label(frame_body,height=100, image =img,bg='#AC7088')
app_image.place(x=10,y=10)

#create name label
name=Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'), fg='black',bg='#AC7088')
name.place(x=125,y=10)

#hour label
hour=Label(frame_body, text="hour", height=1, font=('Ivy 10 bold'), fg='black',bg='#AC7088')
hour.place(x=127,y=40)
#create list to time box
c_hour=Combobox(frame_body,width=2,font=('arial 15'))
#insert values
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0) #initial value will be 00
c_hour.place(x=130,y=59)


#minutes label
min=Label(frame_body, text="minute", height=1, font=('Ivy 10 bold'), fg='black',bg='#AC7088')
min.place(x=177,y=40)
#create list to time box
c_min=Combobox(frame_body,width=2,font=('arial 15'))
#insert values
c_min['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0) #initial value will be 00
c_min.place(x=180,y=59)


#second label
sec=Label(frame_body, text="second", height=1, font=('Ivy 10 bold'), fg='black',bg='#AC7088')
sec.place(x=227,y=40)
#create list to time box
c_sec=Combobox(frame_body,width=2,font=('arial 15'))
#insert values
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0) #initial value will be 00
c_sec.place(x=230,y=59)



#minutes label
period=Label(frame_body, text="period", height=1, font=('Ivy 10 bold'), fg='black',bg='#AC7088')
period.place(x=277,y=40)
#create list to time box
c_period=Combobox(frame_body,width=3,font=('arial 15'))
#insert values
c_period['values']=("AM","PM")
c_period.current(0) #initial value will be 00
c_period.place(x=280,y=59)


#create thread
def activate_alarm():
    t= Thread(target=alarm)
    t.start()
    
def deactivate_alarm():
    print("deactivated",selected.get())
    mixer.music.stop()


selected=IntVar()

#create activate button
rad1= Radiobutton(frame_body,font=('arial 10 bold'),value=1,text="Activate",bg='#AC7088',fg='black',command=activate_alarm, variable=selected)
rad1.place(x=125,y=95)


#ring alarm with current time
def sound():
    mixer.music.load('Soft Music.mp3')
    mixer.music.play()
    selected.set(0)
    
    #create deactivate button
    rad2= Radiobutton(frame_body,font=('arial 10 bold'),value=2,text="Deactivate",bg='#AC7088',fg='black',command= deactivate_alarm , variable=selected)
    rad2.place(x=187,y=95)
    
def alarm():
    while True:
        control=selected.get()
        print(control)
        alarm_hour=c_hour.get()
        alarm_min=c_min.get()
        alarm_sec=c_sec.get()
        alarm_period=c_period.get()
        alarm_period= str(alarm_period).upper()
        
        #extract format
        now=datetime.now()
        
        hour=now.strftime("%I")
        minute=now.strftime("%M")
        second=now.strftime("%S")
        period=now.strftime("%p")
        
        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_min==minute:
                        if alarm_sec==second:
                            print("break")
                            sound()
                            
        sleep(1)

mixer.init()
#alarm()
window.mainloop()
