import turtle
import math

turtle.ht()

def drawFu():
     turtle.pensize(3)
     turtle.speed(2)
     turtle.penup()
     turtle.goto(0,200)
     turtle.pendown()
     turtle.pencolor("red")
     turtle.goto(-200,0)
     turtle.goto(0,-200)
     turtle.goto(200,0)
     turtle.goto(0,200)
     turtle.penup()

     turtle.pensize(6)
     turtle.speed(1)
     turtle.goto(-70,100)
     turtle.pendown()
     turtle.goto(-30,100)
     turtle.penup()
     turtle.goto(-75,80)
     turtle.pendown()
     turtle.goto(-25,80)
     turtle.goto(-25,30)
     turtle.goto(-75,30)
     turtle.goto(-75,-90)
     turtle.penup()
     turtle.goto(-75,0)
     turtle.pendown()
     turtle.goto(-25,0)
     turtle.goto(-25,-70)

     turtle.penup()
     turtle.goto(-5,100)
     turtle.pendown()
     turtle.goto(70,100)
     turtle.penup()
     turtle.goto(-5,80)
     turtle.pendown()
     turtle.goto(-5,30)
     turtle.penup()
     turtle.goto(-5,80)
     turtle.pendown()
     turtle.goto(70,80)
     turtle.goto(70,30)
     turtle.penup()
     turtle.goto(-5,30)
     turtle.pendown()
     turtle.goto(70,30)
     turtle.penup()
     turtle.goto(-5,0)
     turtle.pendown()
     turtle.goto(-5,-90)
     turtle.penup()
     turtle.goto(-5,0)
     turtle.pendown()
     turtle.goto(70,0)
     turtle.goto(70,-90)
     turtle.penup()
     turtle.goto(-5,-45)
     turtle.pendown()
     turtle.goto(70,-45)
     turtle.penup()
     turtle.goto(32.5,0)
     turtle.pendown()
     turtle.goto(32.5,-90)
     turtle.penup()
     turtle.goto(-5,-90)
     turtle.pendown()
     turtle.goto(70,-90)

def drawTiger():
     turtle.speed(20)
     turtle.pensize(3)
     turtle.penup()
     x=-150
     y=50
     turtle.goto(x,y)
     turtle.pendown()
     while y<150:
          y=y+1
          x=-150-math.sqrt(100*100-(y-150)*(y-150))
          turtle.goto(x,y)
     while x<-50:
          x=x+1
          y=150+math.sqrt(100*100-(x+150)*(x+150))
          turtle.goto(x,y)

     turtle.pensize(6)
     turtle.penup()
     x=-232
     y=190
     turtle.goto(x,y)
     turtle.pendown()
     while x<-190:
          x=x+1
          y=math.sqrt(105*105-(x+140)*(x+140))+140
          turtle.goto(x,y)
          
     turtle.penup()
     x=-232
     y=190
     turtle.goto(x,y)
     turtle.pendown()
     while x<-190:
          x=x+1
          y=math.sqrt(105*105-(x+140)*(x+140))+140
          turtle.goto(x,y)
          
     turtle.penup()
     x=-215
     y=195
     turtle.goto(x,y)
     turtle.pendown()
     while x<-195:
          x=x+1
          y=math.sqrt(100*100-(x+135)*(x+135))+135
          turtle.goto(x,y)

     turtle.penup()
     x=-220
     y=176.4
     turtle.goto(x,y)
     turtle.pendown()
     while x<-171:
          x=x+1
          y=0.001*(x+640)*(x+640)
          turtle.goto(x,y)

     turtle.penup()
     x=-214.246
     y=214.246
     turtle.goto(x,y)
     turtle.pendown()
     while x<-196.602:
          x=x+1
          y=-x
          turtle.goto(x,y)

     turtle.pensize(3)
     turtle.penup()
     turtle.goto(-196,131)
     turtle.pendown()
     turtle.circle(18)

     turtle.penup()
     turtle.goto(-146,180)
     turtle.pendown()
     turtle.circle(18)
     #eyes

     turtle.penup()
     x=-179.853
     y=245.44
     turtle.goto(x,y)
     turtle.pendown()
     while x<-120.147:
          x=x+1
          y=-0.05*(x+150)*(x+150)+290
          turtle.goto(x,y)

     turtle.penup()
     x=-245.44
     y=120.147
     turtle.goto(x,y)
     turtle.pendown()
     while y<179.853:
          y=y+1
          x=0.05*(y-150)*(y-150)-290
          turtle.goto(x,y)

     turtle.penup()
     turtle.goto(-199,149)
     turtle.pendown()
     turtle.circle(8)

     turtle.penup()
     turtle.goto(-196,138)
     turtle.pendown()
     turtle.circle(5)
     
     turtle.penup()
     turtle.goto(-149,199)
     turtle.pendown()
     turtle.circle(8)
     
     turtle.penup()
     turtle.goto(-138,192)
     turtle.pendown()
     turtle.circle(5)

     turtle.pensize(2)
     turtle.penup()
     x=-140
     y=140
     turtle.goto(x,y)
     turtle.pendown()
     while x<-120:
          x=x+1
          y=math.sqrt(100-(x+130)*(x+130))+140
          turtle.goto(x,y)

     turtle.penup()
     turtle.goto(-140,120)
     turtle.pendown()
     turtle.circle(10,-180)

     turtle.penup()
     x=-140
     y=120
     turtle.goto(x,y)
     turtle.pendown()
     while x<-120:
          x=x+1
          y=math.exp(0.093*(x+154))+116.3
          turtle.goto(x,y)

#     turtle.penup()
#     x=-200
#     y=88
#     turtle.goto(x,y)
#     turtle.pendown()
#     while x<-128:
#          x=x+1
#          y=128-math.sqrt(47*47-(x+175)*(x+175))
#          turtle.goto(x,y)

#     turtle.penup()
#     x=-128
#     y=128
#     turtle.goto(x,y)
#     turtle.pendown()
#     while x<-81:
#          x=x+1
#          y=175-math.sqrt(47*47-(x+128)*(x+128))
#          turtle.goto(x,y)

     turtle.penup()
     x=-128
     y=128
     turtle.goto(x,y)
     turtle.seth(0)
     turtle.right(45)
     turtle.pendown()
     ang=0
     while ang<=80:
          turtle.forward(1)
          turtle.right(2)
          ang=ang+1

     turtle.penup()
     x=-128
     y=128
     turtle.goto(x,y)
     turtle.seth(0)
     turtle.right(45)
     turtle.pendown()
     ang=0
     while ang<=80:
          turtle.forward(1)
          turtle.left(2)
          ang=ang+1

     turtle.penup()
     x=-59
     y=190
     turtle.goto(x,y)
     turtle.pendown()
     while x<-29:
          x=x+1
          y=100+math.sqrt(100*100-(x+100)*(x+100))
          turtle.goto(x,y)

     turtle.penup()
     x=-171
     y=29
     turtle.goto(x,y)
     turtle.pendown()
     while x>-191:
          x=x-1
          y=100-math.sqrt(100*100-(x+100)*(x+100))
          turtle.goto(x,y)
     
     turtle.penup()
     x=-173
     y=47
     turtle.goto(x,y)
     turtle.pendown()
     while x>-195:
          x=x-1
          y=x+220
          turtle.goto(x,y)

     turtle.penup()
     x=-169
     y=40.3
     turtle.goto(x,y)
     turtle.pendown()
     while x>-180:
          x=x-1
          y=1.3*x+260
          turtle.goto(x,y)

     turtle.penup()
     x=-180
     y=51
     turtle.goto(x,y)
     turtle.pendown()
     while x>-193:
          x=x-1
          y=0.7*x+177
          turtle.goto(x,y)

     turtle.penup()
     x=-48
     y=172
     turtle.goto(x,y)
     turtle.pendown()
     while x<-28:
          x=x+1
          y=x+221
          turtle.goto(x,y)

     turtle.penup()
     x=-50
     y=180
     turtle.goto(x,y)
     turtle.pendown()
     while x<-40:
          x=x+1
          y=1.4*x+250
          turtle.goto(x,y)

     turtle.penup()
     x=-42
     y=168.5
     turtle.goto(x,y)
     turtle.pendown()
     while x<-25:
          x=x+1
          y=0.7*x+200
          turtle.goto(x,y)

     turtle.pensize(6)
     turtle.penup()
     x=100
     y=-100
     turtle.goto(x,y)
     turtle.seth(0)
     turtle.right(45)
     turtle.pendown()
     ang=0
     while ang<=80:
          turtle.forward(1.5)
          turtle.right(1.5)
          ang=ang+1
     turtle.mainloop()
     
               
drawFu()
drawTiger()






