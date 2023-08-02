from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#c0cee7"
    text_color: "#3a6091"
    icon_color: "#1c3d75"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#914b0d"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "PyDream"
                    icon: "git"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#054575"
                    specific_text_color: "#c2e4fc"
                    specific_text_size: 40
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
            
            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 222"
                    halign: "center"
               
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 80, 80, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "PyDream"
                    title_color: "#c2e4fc"
                    text: "Functions Menu"
                    text_color: "#349be3"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    source: "logo.png"

                MDNavigationDrawerLabel:
                    text: "MyPi"

                DrawerClickableItem:
                    icon: "note"
                    right_text: "+"
                    text_right_color: "#4a4939"
                    text: "Diagrams / Schemas"
                    
                DrawerClickableItem:
                    icon: "wifi"
                    right_text: "+"
                    text_right_color: "#4a4939"
                    text: "Digital I/O"

                DrawerClickableItem:
                    icon: "home"
                    right_text: "+"
                    text_right_color: "#4a4939"
                    text: "Joystick"
                    
                DrawerClickableItem:
                    icon: "radar"
                    text: "Settings"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Applications"

                DrawerClickableItem:
                    icon: "car"
                    text: "Remote Car"

                DrawerClickableItem:
                    icon: "music"
                    text: "Drone"
'''


class Example(MDApp):
    title = 'PyDream - Pi making with Py'
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()