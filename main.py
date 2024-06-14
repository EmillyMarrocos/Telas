from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import TelaLogin
from cadastro import TelaCadastro
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        # Definindo a cor de fundo da janela
        Window.clearcolor = (0.68, 0.85, 0.90, 1)  # Cor azul claro

        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='LOGIN'))
        sm.add_widget(TelaCadastro(name='CADASTRO'))
        return sm

if __name__ == '__main__':
    MainApp().run()