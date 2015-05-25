import turtle
class stack:
    def __init__(self):
        self.n=[]
        self.top=0

    def push(self,val):
        self.n.append(val)
        self.top=self.top+1

    def pop(self):
        col=self.n[self.top-1]
        self.n.pop()
        self.top=self.top-1
        return col
    def is_empty(self):
        if self.n==[]:
            return 1
        else:
            return 0

turtle.ht()

def drawtower():
    turtle.tracer(3)
    turtle.setpos(0,250)
    turtle.color("purple")
    turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
    turtle.bgcolor("black")
    turtle.pensize(4)
    turtle.left(90)
    turtle.pendown()
    x=-150
    y=-150
    i=0
    for i in range(3):
        turtle.pencolor("black")
        turtle.setpos(x,y)
        turtle.pencolor("brown")
        turtle.forward(300)
        x=x+200
    turtle.penup()
    turtle.setpos(50,-225)
    turtle.write("A           B             C",True,"center",("Arial",40,"normal"))

def drawrect(l,b,col):
    turtle.color(col)
    turtle.begin_fill()
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()
    
def drawstack(t1,t2,t3):
    turtle.tracer(3)
    turtle.left(90)
    flag=0
    if t1.is_empty():
        flag=1
    else:
        x=-90
        y=-150
        i=0
        while i<t1.top:
            turtle.up()
            turtle.setpos(x,y)
            if t1.n[i]==0: turtle.setpos(-90,y); drawrect(120,30,"red")
            elif t1.n[i]==1: turtle.setpos(-105,y); drawrect(90,30,"cyan")
            elif t1.n[i]==2: turtle.setpos(-120,y); drawrect(60,30,"orange")
            elif t1.n[i]==3: turtle.setpos(-135,y); drawrect(30,30,"yellow")
            y=y+30
            i=i+1
    #print("stack1")
    if t2.is_empty():
        flag=1
    else:
        x=110
        y=-150
        i=0
        while i<t2.top:
            turtle.up()
            turtle.setpos(x,y)
            if t2.n[i]==0: turtle.setpos(110,y); drawrect(120,30,"red")
            elif t2.n[i]==1: turtle.setpos(95,y); drawrect(90,30,"cyan")
            elif t2.n[i]==2: turtle.setpos(80,y);drawrect(60,30,"orange")
            elif t2.n[i]==3: turtle.setpos(65,y);drawrect(30,30,"yellow")
            y=y+30
            i=i+1
    #print("stack2")
    if t3.is_empty():
        #print("popempty")
        flag=1
    else:
        #print("popprint")
        x=310
        y=-150
        i=0
        while i<t3.top:
            turtle.up()
            turtle.setpos(x,y)
            if t3.n[i]==0: turtle.setpos(310,y);drawrect(120,30,"red")
            elif t3.n[i]==1: turtle.setpos(295,y);drawrect(90,30,"cyan")
            elif t3.n[i]==2: turtle.setpos(280,y);drawrect(60,30,"orange")
            elif t3.n[i]==3: turtle.setpos(265,y);drawrect(30,30,"yellow")
            y=y+30
            i=i+1
    #print("stack3")
            
def setright():
    turtle.right(90)

class hanoi:
    def __init__(self):
        self.t1=stack()
        self.t2=stack()
        self.t3=stack()

    def createtower(self,num):
        i=0
        for i in range(num):
            self.t1.push(i)

    def move(self,x,y):
        #print(x,y)
        flag=0
        if x=='a':
            #print("pop")
            col=self.t1.pop()
        elif x=='b':
            col=self.t2.pop()
        elif x=='c':
            col=self.t3.pop()
        #print("pop")
        if y=='a':
            #print("pop")
            if self.t1.is_empty():
                self.t1.push(col)
            else:
                if col>self.t1.n[self.t1.top-1]:
                    self.t1.push(col)
                else:
                    flag=1
        elif y=='b':
            #print("pop")
            if self.t2.is_empty():
                self.t2.push(col)
            else:
                if col>self.t2.n[self.t2.top-1]:
                    self.t2.push(col)
                else:
                    flag=1
        elif y=='c':
            if self.t3.is_empty():
                #print("popmove")
                self.t3.push(col)
            else:
                if col>self.t3.n[self.t3.top-1]:
                    #print("popmove")
                    self.t3.push(col)
                else:
                    flag=1
        if flag==1:
            #print("cannot place bigger disk on top of smaller disk")
            if x=='a':
                self.t1.push(col)
            elif x=='b':
                self.t2.push(col)
            else:
                self.t3.push(col)
            return 1
        else:
            return 0

    def check(self,num):
        flag=0
        if self.t3.top==num:
            flag=0
            '''for i in range(self.t3.top):
                if self.t3.n[i]!=i:
                    flag=1
                    break'''
        else:
            flag=1
        return flag
    
    def solve(self,num):
        self.t1.n=[]; self.t2.n=[]; self.t3.n=[];
        self.t1.top=0; self.t2.top=0; self.t3.top=0;
        turtle.reset()
        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
        drawtower()
        self.createtower(num)
        #print(self.t1.n[0],self.t1.n[1],self.t1.n[2])
        drawstack(self.t1,self.t2,self.t3)
        s=input("enter n")
        if s=='n':
            if num%2==0:
                while self.check(num):
                    chk=0
                    s=input("enter n")
                    if s=='n':
                        if self.t1.is_empty(): self.move('b','a')
                        else: chk=self.move('a','b')
                        if chk: self.move('b','a')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(1)
                        turtle.delay(5)
                        turtle.tracer(3)
                    chk=0
                    s=input("enter n")
                    if s=='n':
                        if self.t2.is_empty(): self.move('c','a')
                        else: chk=self.move('a','c')
                        if chk: self.move('c','a')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(1)
                        turtle.delay(5)
                        turtle.tracer(3)
                    chk=0
                    s=input("enter n")
                    if s=='n':
                        if self.t2.is_empty(): self.move('c','b')
                        else: chk=self.move('b','c')
                        if chk: self.move('c','b')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(1)
                        turtle.delay(5)
                        turtle.tracer(3)
            else:
                while self.check(num):
                    chk=0
                    s=input("enter n")
                    if s=='n':
                        if self.t1.is_empty(): self.move('c','a')
                        else: chk=self.move('a','c')
                        if chk: self.move('c','a')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(0)
                        turtle.delay(5)
                        turtle.tracer(3)
                    chk=0
                    s=input("enter n")
                    if s=='n':
                        #flag=0
                        if self.t1.is_empty(): self.move('b','a')
                        else: chk=self.move('a','b')
                        if chk: self.move('b','a')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(0)
                        turtle.delay(5)
                        turtle.tracer(3)
                    chk=0
                    s=input("enter n:")
                    if s=='n':
                        if self.t3.is_empty(): self.move('b','c')
                        else: chk=self.move('c','b')
                        if chk: self.move('b','c')
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        turtle.tracer(0)
                        turtle.delay(5)
                        turtle.tracer(3)
                
    def play(self,num):
        turtle.bgcolor("black")
        turtle.setpos(0,250)
        turtle.color("purple")
        drawtower()
        self.createtower(num)
        drawstack(self.t1,self.t2,self.t3)
        flag=0
        moves=1
        m=[]
        while flag==0:
           #turtle.write("MOVE:   ","center",("Arial",30,"normal"))
            print("\n")
            s=input("ENTER s TO SEE SOLUTION: ")
            if s=='s': self.solve(num);break;
            else:
                m1=input("ENTER MOVE FROM: ")
                m2=input("ENTER MOVE TO: ")
                if m1=='a' and self.t1.is_empty(): print("NO DISKS IN TOWER"); continue
                elif m1=='b' and self.t2.is_empty(): print("NO DISKS IN TOWER"); continue
                elif m1=='c' and self.t3.is_empty(): print("NO DISKS IN TOWER"); continue
                chk=self.move(m1,m2)
                if chk:
                    print("cannot place bigger disk on top of smaller disk")
                    turtle.reset()
                    turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                    drawtower()
                    drawstack(self.t1,self.t2,self.t3)
                    continue
                else:
                    if self.check(num)==0:
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                        flag=1
                        break
                    else:
                        turtle.reset()
                        turtle.write("TOWER OF HANOI",True,"center",("Arial",40,"normal"))
                        drawtower()
                        drawstack(self.t1,self.t2,self.t3)
                moves=moves+1
        if flag==1:
            print("YOU SOLVED IT IN ",moves," MOVES.")

                   
            
h=hanoi()
h.play(4)


        
                        
                    







        
            

        
