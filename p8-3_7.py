from turtle import *
n = 7
for i in range(n):
    forward(100)
    left(360/n)
left(360/n * 2)
for i in range(n):
    forward(180)
    right(360/n * 2)
done()
