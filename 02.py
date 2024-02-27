# Imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Grid Layout Class
class Grid(GridLayout):
    # Creating a Function Inheritance 
    def __init__(self, **kwagrs):
        super(Grid, self).__init__(**kwagrs)
        
        # Number of Coloums in the Grid Layout of the Application
        self.cols = 2
        
        # Label
        self.add_widget(Label(text = 'Name : '))
        self.name = TextInput(multiline = False)
        
        # add_widget function to push the component to the screen 
        self.add_widget(self.name)
        
        # Text Input Box
        self.add_widget(Label(text='Email : '))
        self.email = TextInput(multiline = False)
        self.add_widget(self.email)
        
        # Text Input Box
        self.add_widget(Label(text='Phone Number : '))
        self.phone_number = TextInput(multiline= False)
        self.add_widget(self.phone_number)
        
        # Submit Button with the on_press keyword to trigger thee pressed function !
        self.submit = Button(text='Submit !', font_size=20)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    # Creating the Pressed function 
    def pressed(self, instance):
        # Print the output on the Terminal
        print(f'''
Hey ! {self.name.text}
Email ID : {self.email.text}
Phone Number : {self.phone_number.text}
''')
        # Insert the output on the Screen
        self.add_widget(Label(text=f'''
Hey ! {self.name.text}
Email ID : {self.email.text}
Phone Number : {self.phone_number.text}
'''))
        
        # Clear the Input boxes
        self.name.text, self.email.text, self.phone_number.text = "", "", ""
        
# App Class
class MyApp(App):
    # Build Function
    def build(self):
        return Grid()
    
# Running Instance
if __name__ == '__main__':
    MyApp().run()