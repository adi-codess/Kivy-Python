# Imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

# Application Class
class MyApp(App):
    # Build Function
    def build(self):
        # Label or Text 
        label = Label(text='Hello, World !')
        # Returnnig the Label
        return label

# Running Instance 
if __name__ == '__main__':
    MyApp().run()