from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from login import TelaLogin
from cadastro import TelaCadastro

class MainApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())  # Utilizando NoTransition para evitar transições

        # Criando as instâncias das telas
        tela_login = TelaLogin(name='LOGIN', manager=sm)
        tela_cadastro = TelaCadastro(name='CADASTRO', manager=sm)

        # Adicionando as telas ao ScreenManager
        sm.add_widget(tela_login)
        sm.add_widget(tela_cadastro)

        return sm

if __name__ == '__main__':
    MainApp().run()