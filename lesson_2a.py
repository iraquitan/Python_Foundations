# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: Python_Foundations
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: lesson_2a
 * Date: 10/1/15
 * Time: 11:31 PM
 * To change this template use File | Settings | File Templates.
"""
import turtle


def draw_square(ttl):
    for i in range(4):
        ttl.forward(100)
        ttl.right(90)


def draw_circle():
    ttl = turtle.Turtle()
    ttl.shape('circle')
    ttl.color('yellow', 'blue')
    ttl.speed(3)
    ttl.circle(100)


def draw_triangle():
    ttl = turtle.Turtle()
    ttl.shape('triangle')
    ttl.color('yellow', 'blue')
    ttl.speed(3)
    for i in range(3):
        ttl.forward(100)
        ttl.right(120)


def draw_shape(ttl, n):
    for i in range(n):
        ttl.forward(100)
        ttl.right(360./n)


def draw_lozenge(ttl, size=100):
    for i in range(4):
        if i % 2 == 0:
            ttl.forward(size)
            ttl.right(45)
        else:
            ttl.forward(size)
            ttl.right(180-45)

window = turtle.Screen()
window.bgcolor('green')

sqr = turtle.Turtle()
sqr.shape('square')
sqr.color('yellow', 'blue')
sqr.speed(10)
degree = 10
dg_count = 0
while dg_count < 360:
    draw_lozenge(sqr)
    sqr.right(degree)
    dg_count += degree
sqr.right(90)
sqr.forward(200)
sqr.left(90)
draw_lozenge(sqr, 50)
sqr.right(90)
sqr.forward(100)

window.exitonclick()
