from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Mygrid(GridLayout):
    # init infinit keywords by using **kwargs
    def __init__(self, **kwargs):
        #call GridLayout constructor
        super(Mygrid, self).__init__(**kwargs) 
        # build columns
        self.cols = 1
        # Create top grid
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        #add widgets Username
        self.top_grid.add_widget(Label(text='Username: '))
        #add inputbox 
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        #add widgets IP
        self.top_grid.add_widget(Label(text='Ip Address: '))
        #add inputbox 
        self.ip = TextInput(multiline=False)
        self.top_grid.add_widget(self.ip)
        self.add_widget(self.top_grid)
        #button
        self.submit = Button(text='submit', font_size=32)
        self.submit.bind(on_press=self.press) 
        self.add_widget(self.submit)
    def press(self,instance):
        name = self.name.text
        ips = self.ip.text
        self.add_widget(Label(text=f'hello\r{name} , your ip is {ips}'))
        #Clear boxs
        self.name.text = ''
        self.ip.text = ''



class Myapp(App):
    def build(self):
        return Mygrid()



if __name__ == '__main__':
    Myapp().run()