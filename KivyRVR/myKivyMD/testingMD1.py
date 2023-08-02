from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp


# Designate Our .kv design file
Builder.load_file('testingMD1.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(MDApp):  #Inject une App type MDApp over the same layout kivy
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()

