from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.clearcolor = (0.6, 0.8, 1, 1) #Cor Azul Claro

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout principal vertical
        self.orientation = "vertical"
        self.spacing = 20
        self.padding = [50, 50]

        #Ícone
        self.icon = Image(source="/Users/aluno.sesipaulista/Documents/Telas/img/img_icon.jpeg", size_hint=(None, None), size=(100,100))
        self.add_widget(self.icon)

        #Email
        self.email = TextInput(hint_text="Email", multiline=False, font_size=20)
        self.add_widget(self.email)

        #Senha
        self.senha = TextInput(hint_text="Senha", multiline=False, password=True, font_size=20)
        self.add_widget(self.senha)

        #Botão de Cadastro
        self.botao_cadastro = Button(text="Cadastrar", size_hint=(None, None), size=(150, 50), font_size=20)
        self.botao_cadastro.bind(on_press=self.cadastro)
        self.add_widget(self.botao_cadastro)

        #Mensagens de erro
        self.error_label = Label(text= '', color=(1, 0, 0, 1), font_size=16)
    
    def load_image(self, instance):
        #Carregar a imagem de perfil
        pass

    def cadastro(self, instance):
        email = self.email.text
        senha = self.senha.text

        #Verificação
        if email and senha:
            self.error_label.text = "Cadastro realizado com sucesso!"
        else:
            self.error_label.text = "Preencha todos os campos"

class AppCadastro(App):
    def build(self):
        return TelaCadastro
    
if __name__ == "__main__":
    AppCadastro().run()