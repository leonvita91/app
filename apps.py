from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
# use to target the .kv files
from kivy.lang import Builder

# target any kv files
Builder.load_file('login.kv')


class Mygrid(Widget):
    # set kv value to none
    name = ObjectProperty(None)
    password = ObjectProperty(None)
    result = ObjectProperty(None)

    #interact with button
    def press(self):
        name = self.name.text
        password = self.password.text
        result = self.result.text

        if name == 'leon':
            print(f'welcome: {name} you password is {password}')
        else:
            result = 'Wrong Input'
            print(result)
            
        self.name.text = ''
        self.password.text = ''



class Myapp(App):
    def build(self):
        return Mygrid()

if __name__ == '__main__':
    Myapp().run()






    # # # init infinit keywords by using **kwargs
    # # def __init__(self, **kwargs):
    # #     #call GridLayout constructor
    # #     super(Mygrid, self).__init__(**kwargs) 
    # #     # build columns
    # #     self.cols = 1
    # #     self.padding = 300
    # #     # self.spacing = 40
    # #     # Create top grid
    # #     self.top_grid = GridLayout()
    # #     self.top_grid.cols = 2
    # #     #add widgets Username
    # #     self.top_grid.add_widget(Label(text='Username: ',font_size=32,
    # #     size_hint_y=None,
    # #     height=100))
    # #     #add inputbox
    # #     self.name = TextInput(multiline=False,font_size=32,
    # #     size_hint_y=None,
    # #     height=100)
    # #     self.top_grid.add_widget(self.name)
    # #     #add widgets IP
    # #     self.top_grid.add_widget(Label(text='Ip Address: ',font_size=32,
    # #     size_hint_y=None,
    # #     height=100))
    # #     #add inputbox
    # #     self.ip = TextInput(multiline=False,font_size=32,
    # #     size_hint_y=None,
    # #     height=100)
    # #     self.top_grid.add_widget(self.ip)
    # #     self.add_widget(self.top_grid)
    # #     #button
    # #     self.submit = Button(text='submit',
    # #     font_size=32,
    # #     size_hint_y=None,
    # #     height=100,
    # #     size_hint_x=None,
    # #     width=200)
    # #     self.submit.bind(on_press=self.press) 
    # #     self.add_widget(self.submit)
    
    # #interact with button
    # def press(self,instance):
    #     name = self.name.text
    #     ips = self.ip.text
    #     if name == 'leon' and ips == '1010':
    #         self.add_widget(Label(text=f'hello\r{name} , your ip is {ips}'))
    #     else:
    #         self.add_widget(Label(text='Username or Password is not correct'))

    #     #Clear boxs
    #     self.name.text = ''
    #     self.ip.text = ''


