from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

Builder.load_file("07.kv")

class MyWidgetLayout(Widget):
    name = ObjectProperty(None)
    task = ObjectProperty(None)
    def pressed(self):
        name = self.name.text
        task = self.task.text
        print(f"Name : {name}\nTask : {task}")
        self.name.text, self.task.text = '', ''

class MyApp(App):
    def build(self):
        return MyWidgetLayout()

if __name__ == '__main__':
    MyApp().run()