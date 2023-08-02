from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

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



<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Screen 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        OneLineListItem:
            text: "Screen 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"


MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "scr 1"   
                
                MDLabel:
                    text: "Screen 111"
                    halign: "center"
                                 
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
            screen_manager: screen_manager
            nav_drawer: nav_drawer
              
                
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
                    text: "Diagrams1"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 1"
                    
                DrawerClickableItem:
                    icon: "wifi"
                    right_text: "+"
                    text_right_color: "#4a4939"
                    text: "Digital I/O"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"
                        
                DrawerClickableItem:
                    icon: "home"
                    right_text: "+"
                    text_right_color: "#4a4939"
                    text: "Joystick"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 1"                    
                    
                DrawerClickableItem:
                    icon: "radar"
                    text: "Settings"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"
                        
                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Applications"
                        
                DrawerClickableItem:
                    icon: "car"
                    text: "Remote Car"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 3"
                        
                DrawerClickableItem:
                    icon: "music"
                    text: "Drone"
                    on_press:
                        root.nav_drawer.set_state("close")
                        root.screen_manager.current = "scr 2"                    
'''

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()