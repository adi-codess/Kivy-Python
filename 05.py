# Imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


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
        # Insert the output on the Screen
#        self.add_widget(
#            Label(
#                text=f"""
#Hey ! {self.name.text}
#Email ID : {self.email.text}
#Anything Value : {self.anything.text}
#"""
#            )
#        )

        # Clear the Input boxes
        self.name.text, self.email.text, self.anything.text = "", "", ""

    # Created a Dimensions Function


# App Class
class MyApp(App):
    # Build Function
    def build(self):
        return WidgetLayout()


# Running Instance
if __name__ == "__main__":
    MyApp().run()
