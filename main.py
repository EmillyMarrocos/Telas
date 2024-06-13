from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from login import TelaLogin
from cadastro import TelaCadastro

class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='LOGIN'))
        sm.add_widget(TelaCadastro(name='CADASTRO'))
        return sm
    
if __name__ == '__main__':
    Main().run()