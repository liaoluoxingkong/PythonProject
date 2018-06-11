#coding=utf8
from tkinter import *
import time
from datetime import *
from turtle import *  

def Skip(step):  
    penup()  
    forward(step)  
    pendown()  

def mkHand(name, length):  
    #注册Turtle形状，建立表针Turtle  
    reset()  #清空当前窗口，并重置位置等信息为默认值  
    Skip(-length*0.1)  
    begin_poly()  
    forward(length*1.1)  
    end_poly()  
    handForm = get_poly()  
    register_shape(name, handForm)   

def Init():  
    global secHand, minHand, hurHand, printer  
    mode("logo")# 重置Turtle指向北  
    #建立三个表针Turtle并初始化  
    mkHand("secHand", 135)  
    mkHand("minHand",  110)  
    mkHand("hurHand", 90)  
    secHand = Turtle()  
    secHand.shape("secHand")  
    minHand = Turtle()  
    minHand.shape("minHand")  
    hurHand = Turtle()  
    hurHand.shape("hurHand")  
    for hand in secHand, minHand, hurHand:  
        hand.shapesize(1, 1, 3)  
        hand.speed(0)  
    #建立输出文字Turtle  
    printer = Turtle()  
    printer.hideturtle()  
    printer.penup()  

def SetupClock(radius):  
    #建立表的外框  
    reset()  
    pensize(7)  
    for i in range(60):  
        Skip(radius)  
        if i % 5 == 0:  
            forward(20)  
            Skip(-radius-20)  
        else:  
            dot(5)  
            Skip(-radius)  
        right(6)  

def Week(t):      
    week = ["星期一", "星期二", "星期三",  
            "星期四", "星期五", "星期六", "星期日"]  
    return week[t.weekday()]  

def Date(t):  
    y = t.year  
    m = t.month  
    d = t.day  
    return "%s %d %d" % (y, m, d)  

def Tick():  
    #绘制表针的动态显示  
    t = datetime.today()  
    second = t.second + t.microsecond*0.000001  
    minute = t.minute + second/60.0  
    hour = t.hour + minute/60.0  
    secHand.setheading(6*second) #设置朝向，每秒转动6度  
    minHand.setheading(6*minute)  
    hurHand.setheading(30*hour) 
    zodiac=("猴鸡狗猪鼠牛虎兔龙蛇马羊")

    tracer(False)  #不显示绘制的过程，直接显示绘制结果  
    printer.forward(65)  
    printer.write(Week(t), align="center",  
                  font=("Courier", 14, "bold"))  
    printer.back(130)  
    printer.write(Date(t), align="center",  
                  font=("Courier", 14, "bold"))  
    printer.back(50)  
    printer.write(zodiac[t.year%12]+"年", align="center",  
                  font=("Courier", 14, "bold"))  
    printer.home()  
    tracer(True)  

    ontimer(Tick, 1000)#1000ms后继续调用tick  
    
def turmain(event):  
    tracer(False) #使多个绘制对象同时显示  
    Init()  
    SetupClock(160)  
    tracer(True)  
    Tick()  


def tgdz(t):
    sky=("庚辛壬癸甲乙丙丁戊己")
    earth=("申酉戌亥子丑寅卯辰巳午未")
    return "%s%s年"%(sky[t.year%10],earth[t.year%12])

def pr(t):
    PRyear={0:"平年",1:"闰年"}
    judgePR=t.year%4==0 and t.year%100!=0 or t.year%400==0    
    return str(PRyear[judgePR])


class Watch(Frame):
    msec = 1000
    ti=datetime.today()
    def __init__(self, parent=None, **kw):
            Frame.__init__(self, parent, kw)
            self._running = False
            self.timestr1 = StringVar()
            self.timestr2 = StringVar() 
            self.timestr3 = StringVar()
            self.timestr4 = StringVar()
            self.makeWidgets()
            self.flag  = True
    def makeWidgets(self):
        l1 = Label(self, textvariable = self.timestr1)
        l2 = Label(self, textvariable = self.timestr2) 
        l3 = Label(self, textvariable = self.timestr3) 
        l4 = Label(self, textvariable = self.timestr4) 
        l1.pack()
        l2.pack() 
        l3.pack()
        l4.pack()
    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)
    def _settime(self):
        ti=datetime.today()
        today1 = str("{0}-{1}-{2}".format(ti.year,ti.month,ti.day))
        time1 = str("{0}:{1}:{2}".format(ti.hour,ti.minute,ti.second))
        self.timestr1.set(today1)
        self.timestr2.set(time1)                 
        self.timestr3.set(tgdz(ti))
        self.timestr4.set(pr(ti))
    def start(self):
        self._update()
        self.pack(side = TOP)
        
        
if __name__ == '__main__':
    def main():
        root = Tk()
        root.title('clock')
        root['bg']="#00FFFF"
        root.geometry('250x150')
        frame1 = Frame(root)
        frame1.pack(side = BOTTOM)
        mw = Watch(root)
        mywatch = Button(frame1, text = '时钟', command = mw.start)
        mywatch.pack(side = LEFT)
        root.bind('<Double-Button-1>', turmain)
        w = Label(root,text="双击打开模拟钟表")
        w.config(width =18,bg="#00FFFF")
        w['anchor'] ='center'
        w.pack()
        root.mainloop()
    main()