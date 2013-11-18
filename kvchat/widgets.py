from os.path import realpath, dirname, join

from kivy import require
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, \
    StringProperty
from kivy.animation import Animation
require("1.7.2")

file_location = dirname(realpath(__file__))
Builder.load_file(join(file_location, 'widgets.kv'), rulesonly=True)


class InitWidget(Widget):
    '''
    InitWidget is a standard widget with the on_init event.
    '''
    __events__ = ('on_init', )

    def __init__(self, **args):
        super(InitWidget, self).__init__(**args)
        self.dispatch('on_init')

    def on_init(self):
        pass


class AutosizeLabel(InitWidget, Label):
    '''
    AutosizeLabel takes the size of the text inside.
    By default, it expands horizontally.
    If width is specified, it expands vertically.

    Not sure if this is the best way to implement it, though :/
    '''
    def on_init(self):
        # This is copy-pasta'd from a StackOverflow answer.
        self.bind(width=lambda s, w: s.setter('text_size')(s, (w, None)))
        self.bind(texture_size=self.setter('size'))


class ClickWidget(Widget):
    '''
    ClickWidget is a clickable widget.
    When clicked, the background changes color.
    It's supposed to be used with child widgets.
    '''
    r = NumericProperty(0.1)
    g = NumericProperty(0.2)
    b = NumericProperty(0.3)
    a = NumericProperty(0)
    color = ReferenceListProperty(r, g, b, a)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.a = 1
        return super(ClickWidget, self).on_touch_up(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            Animation(a=0, d=.25, t='out_quad').start(self)
        return super(ClickWidget, self).on_touch_up(touch)
