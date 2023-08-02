from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
# Designate Our .kv design file
Builder.load_file('animations.kv')

class MyLayout(Widget):

    def animate_it(self, widget, *args):
        self.ids.my_label.text = "You Release The Button!"

        animate = Animation(
           background_color=(255,1,1,100), duration=2)

        animate += Animation(
            size_hint =(1,1), duration=2)

        animate += Animation(
            size_hint =(0.5,0.5))

        animate.start(widget)

        self.ids.my_label.text = "You Release The Button_END!"


    def hello_on(self):
        self.ids.my_label.text = "You Pressed The Button!"


class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()