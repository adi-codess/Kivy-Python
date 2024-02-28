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

        # Number of Columns in the Grid Layout of the Application
        self.cols = 1

        # Creating a Inherited Grid for the Input Boxes Layout
        # To customize the height and width of the grid 
        self.form_grid = GridLayout(
            row_force_default = True,
            col_force_default = True,
            col_default_width = 500,
            row_default_height = 150,            
        )
        self.form_grid.cols = 2

        # Label
        self.form_grid.add_widget(
            Label(
                text="Name : ",
            )
        )
        self.name = TextInput(
            multiline=False, size_hint_x=None, size_hint_y=None, width=700, height=100
        )
        self.form_grid.add_widget(self.name)

        # Text Input
        self.form_grid.add_widget(Label(text="Email : "))
        self.email = TextInput(
            multiline=False, size_hint_x=None, size_hint_y=None, width=700, height=100
        )
        self.form_grid.add_widget(self.email)

        # Text Input
        self.form_grid.add_widget(Label(text="Phone Number : "))
        self.phone_number = TextInput(
            multiline=False, size_hint_x=None, size_hint_y=None, width=700, height=100
        )
        self.form_grid.add_widget(self.phone_number)

        # Adding the Form Layout Grid to the Screen
        self.add_widget(self.form_grid)

        # Submit Button with the on_press keyword to trigger thee pressed function !
        self.submit = Button(
            text="Submit !",
            font_size=20,  
            # Size_hint is an Important Property to reset the X and Y axis.
            size_hint_x=None,
            size_hint_y=None,
            # Then we can set height and width.
            # The width and height are given in pixels
            width=200,
            height=100,
        )
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        # Creating the Pressed function

    def pressed(self, instance):
        # Print the output on the Terminal
        print(
            f"""
Hey ! {self.name.text}
Email ID : {self.email.text}
Phone Number : {self.phone_number.text}
"""
        )
        # Insert the output on the Screen
        self.add_widget(
            Label(
                text=f"""
Hey ! {self.name.text}
Email ID : {self.email.text}
Phone Number : {self.phone_number.text}
"""
            )
        )

        # Clear the Input boxes
        self.name.text, self.email.text, self.phone_number.text = "", "", ""

    # Created a Dimensions Function


# App Class
class MyApp(App):
    # Build Function
    def build(self):
        return Grid()


# Running Instance
if __name__ == "__main__":
    MyApp().run()
