# Imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

# Used to write the Kivy Design Language directly inside the Python file
Builder.load_string('''
# Kivy Design Language
''')

# Used to load a specific Kivy Design File
Builder.load_file("my.kv")

# Widget Layout Class
class WidgetLayout(Widget):    
    
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    anything = ObjectProperty(None)
    
    # Creating the Pressed function    
    def pressed(self):
        # Print the output on the Terminal
        print(
            f"""
Hey ! {self.name.text}
Email ID : {self.email.text}
Anything Value : {self.anything.text}
"""
        )
        # Clear the Input boxes
        self.name.text, self.email.text, self.anything.text = "", "", ""

# App Class
class MyApp(App):
    # Build Function
    def build(self):
        return WidgetLayout()

# Running Instance
if __name__ == "__main__":
    MyApp().run()