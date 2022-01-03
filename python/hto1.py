import turtle
from math import sqrt

t = turtle.Turtle()

t_n = turtle.textinput("Where do you want to travel  ","Enter name of the celestial body")
ort = float(turtle.numinput("Enter orbital radius in au from star to "+t_n,"Enter orbital radius in au from star to "+t_n))


#Get the oribtal radius of the target planer in AU and assign it to a variable named ort
#t_n = input("Where do you want to travel  ")
#ort = float(input("Enter orbital radius in au from star to "+t_n))

#Calculate semi major axis of the hto. Formula smhto = (ort+1)/2
smhto = (ort+1)/2
print("Semi major axis of hohmann transfer orbit ",smhto)

#Calculate the period (p) of the hto. Formula phto*phto = smhto*smhto*smhto. phto = sqrt(smhto*smhto*smhto) in years
phto = sqrt(smhto*smhto*smhto)
print ("Period of hohmann transfer orbit ",phto," years")
#Calculate the ideal relative position of Earth and target body.
#Formula1 Target Body's period ptgt = sqrt (ort*ort*ort)
ptgt = sqrt(ort*ort*ort)
print ("Peroid of ", t_n," " ,ptgt," years")
#Formula2 Angular Travel of Target body for half of phto angDist = (360*phto)/(2*ptgt)
angDist = (360*phto)/(2*ptgt)
print ("Angular travel of ",t_n," during your travel ",angDist)
#Formula3 Ideal Angle between earth and target at launch angIdeal = 180-angDist
angIdeal = 180-angDist

print ("You will take ",(phto/2)," years to reach ",t_n)
#Print time to reach the target body - (phto/2)
print ("ideal angle between earth and ",t_n," at launch - angIdeal ",angIdeal) 
#Print ideal angle between earth and target body at launch - angIdeal

#Draw earth orbit as a circle in brown color with radius 50
#Draw target body's orbit as a circle in blue color with radios 100
#Draw Sun as a filled circle of yellow color with radius 5
#Draw an elliptical orbit from earth orbit to target body orbit
#Draw a horizontal line
#Draw an angular line with  to indicate the position of target body at launch
import math



def circle(r):
    t.penup()
    t.right(90)
    t.forward(r)
    t.pendown()    
    t.left(90)
    t.circle(r)
    t.penup()
    t.left(90)
    t.forward(r)
    t.right(90)
    #t.left(r)

def solidcircle(r,col):
    t.penup()
    t.right(90)
    t.forward(r)
    t.pendown()    
    t.left(90)
    t.fillcolor(col)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(r)
    t.right(90)



def ellipse(a, b,h=None, k=None):
    myturtle = turtle.Turtle()
    if h is None:
        h = 0
    if k is None:
        k = 0

    angle = 360
    converted_angle = angle*0.875
    for i in range(int(converted_angle)+1):
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()
        myturtle.setposition(h+a*math.cos(i/50), k+b*math.sin(i/50))   
    
  
t.pencolor("blue") 
circle(100)
t.pencolor("blue") 
circle(200)

t.pencolor("yellow")  
solidcircle(15,"yellow")
t.forward(100)
t.pencolor("blue")
solidcircle(5,"blue")
t.backward(100)
t.left (angIdeal)
t.forward (200)
t.pencolor("red")
solidcircle(2.5,"red")
t.backward(200)
t.pendown()
t.pencolor("black")
t.forward(225)
t.backward(225)
t.right(angIdeal )
t.forward(225)
t.backward(225)
t.penup()
# c = 150-100
# semi minor b = sqrt of a2 - c2
smi = sqrt(150*150 - 50*50)
ellipse(150,smi,-50,0)
t.penup()
t.goto(-40, 300)
t.pendown()
t.write("Mission to "+t_n)
t.penup()
t.goto(0,-100)
t.pendown()
t.write("earth orbit")
t.penup()
t.goto(-90,150)
t.pendown()
t.write("Hohman transfer orbit")
t.penup()
t.goto(-200,250)
t.pendown()
t.write(("You will take "+str(round(phto/2*365,1))+" days to reach "+t_n))
t.penup()
t.goto(20,20)
t.pendown()
t.write("when rocket at launch Earth and "+t_n+" at"+str(round(angIdeal,2))+"°")
turtle.hideturtle()
turtle.done()





