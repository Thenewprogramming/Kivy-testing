from kivy import require
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.textinput import TextInput
require("1.7.2")

from widgets import ClickWidget


class Message(ClickWidget):
    #TODO: Copy/Paste bubble.
    text = StringProperty("<None>")


class KvChat(App):
    messages = ListProperty([])
    max_messages = NumericProperty(50)

    def add_message(self, text):
        #TODO: Removing and re-adding widgets should be unnessecary.
        self.messages = messages = ([Message(text=text)] +
                                    self.messages[:self.max_messages])
        self.root.grid.clear_widgets()
        for message in messages:
            self.root.grid.add_widget(message)

    def send(self):
        text = self.root.input.text
        if not text:
            return
        self.root.input.text = ""
        self.add_message(text)

if __name__ == "__main__":
    KvChat().run()
