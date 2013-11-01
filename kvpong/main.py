from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ReferenceListProperty, NumericProperty
from kivy.vector import Vector
from random import randint
require("1.7.2")

class Ball(Widget):
    vel_x = NumericProperty(0)
    vel_y = NumericProperty(0)
    vel = ReferenceListProperty(vel_x, vel_y)

    def serve(self):
        self.center = self.parent.center
        print(self.center)
        self.vel = Vector(4, 0).rotate(randint(0, 360))

    def move(self):
        self.pos = Vector(*self.vel) + self.pos

        if self.x <= 0 or self.right >= self.parent.width:
            self.vel_x *= -1

        if self.y <= 0 or self.top >= self.parent.height:
            self.vel_y *= -1

class Paddle(Widget):
    def bounce(self):
        if self.collide_widget(self.parent.ball):
            self.parent.ball.vel_x = -1

class Root(Widget):
    def update(self, idk):
        self.ball.move()
        #self.paddle_left.bounce()
        #self.paddle_right.bounce()

    def on_touch_move(self, touch):
        if touch.x < self.center_x:
            self.paddle_left.center_y = touch.y
        if touch.x > self.center_x:
            self.paddle_right.center_y = touch.y

class KvPong(App):
    def build(self):
        widget = Root()
        widget.ball.serve()
        Clock.schedule_interval(widget.update, 1 / 60)
        return widget

if __name__ == "__main__":
    KvPong().run()
