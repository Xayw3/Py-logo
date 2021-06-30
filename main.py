from tkinter import *
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("Black")


pen = turtle.Turtle()

pen.speed(15)

pen.color("White")

pen.width(30)
tut = turtle.Screen()

pen.right(-135)
pen.forward(140)
pen.backward(100)

pen.right(255)
pen.forward(150)
pen.backward(150)
pen.right(-255)
pen.backward(40)

pen.right(45)
pen.forward(100)

pen.right(90)
pen.forward(80)
pen.backward(80)
pen.left(90)
pen.backward(100)

pen.right(90)
pen.forward(80)
pen.backward(80)

pen.right(90)
pen.forward(100)

pen.right(-90)
pen.forward(80)

pen.penup

cv = turtle.getcanvas()
cv.postscript(file="logo.ps", colormode='color')

import subprocess
cmd = r'C:\Users\Edgar°\Desktop\kursi\python\day-7\ImageMagick-7.1.0-2-portable-Q16-HDRI-x64\magick.exe C:\Users\Edgar°\Desktop\kursi\python\day-7\logo.ps C:\Users\Edgar°\Desktop\kursi\python\day-7\logo.png'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
result = p.communicate()[0]
print(result.decode('cp866'))

turtle.done()