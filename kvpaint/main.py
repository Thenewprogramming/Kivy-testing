from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import ReferenceListProperty, NumericProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import random, randint
require("1.7.2")

class Paint(Widget):
    def draw_circle(self, pos):
        with self.canvas:
            Color(random(), random(), random())
            d = randint(10, 100)
            Ellipse(pos=(pos[0] - d / 2, pos[1] - d / 2), size=(d, d))

    def on_touch_down(self, touch):
        self.draw_circle(touch.pos)
        self.line = Line(points=[touch.x, touch.y], width=10)
        self.canvas.add(self.line)

    def on_touch_move(self, touch):
        self.line.points += [touch.x, touch.y]

class Text(Label):
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    vel = ReferenceListProperty(vel_x, vel_y)

    def reset(self):
        self.center = self.parent.center
        self.vel = Vector(4, 0).rotate(randint(0, 360))

    def move(self, idk):
        self.pos = Vector(*self.vel) + self.pos

        if self.y <= 0 or self.top >= self.parent.height:
            self.vel_y *= -1

        if self.x <= 0 or self.right >= self.parent.width:
            self.vel_x *= -1

class KvPaint(App):
    def build(self):
        widget = self.root

        widget.text.reset()
        Clock.schedule_interval(widget.text.move, 1.0 / 60.0)

        def clear(idk):
            print(idk)
            widget.paint.canvas.clear()
            widget.text.reset()
        widget.clearbtn.bind(on_release=clear)

if __name__ == "__main__":
    KvPaint().run()
