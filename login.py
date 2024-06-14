from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=[50, 50, 50, 50], spacing=20)
        self.add_widget(layout)

        # Ícone de perfil centralizado
        image_layout = BoxLayout(size_hint_y=None, height=150, padding=[50, 0, 50, 0], spacing=10)
        image_layout.add_widget(Label())  # Espaço em branco à esquerda do ícone
        image_layout.add_widget(Image(source='/Users/emill/Documents/Telas/img/img_icon.png', size_hint=(None, None), size=(100, 100)))
        image_layout.add_widget(Label())  # Espaço em branco à direita do ícone
        layout.add_widget(image_layout)

        # Email
        self.email = TextInput(hint_text='E-mail', multiline=False, font_size=20, size_hint_y=None, height=40)
        layout.add_widget(self.email)

        # Senha
        self.senha = TextInput(hint_text='Senha', multiline=False, password=True, font_size=20, size_hint_y=None, height=40)
        layout.add_widget(self.senha)

        # Botão de login
        btn_login = Button(text='LOGIN', size_hint_y=None, height=40, font_size=16)
        btn_login.bind(on_press=self.login)
        layout.add_widget(btn_login)

        # Botões "Cadastrar" e "Login"
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)
        btn_cadastro = Button(text='CADASTRE-SE', font_size=14)
        btn_cadastro.bind(on_press=self.ir_para_cadastro)
        button_layout.add_widget(btn_cadastro)
        
        layout.add_widget(button_layout)

        # Mensagens de erro
        self.error_label = Label(text='', color=(1, 0, 0, 1), font_size=14)
        layout.add_widget(self.error_label)

    def login(self, instance):
        email = self.email.text
        senha = self.senha.text

        # Verificação de login (exemplo simples)
        if email == 'usuario@email.com' and senha == 'senha123':
            self.error_label.text = 'Login bem-sucedido!'
        else:
            self.error_label.text = 'Credenciais inválidas'

    def ir_para_cadastro(self, instance):
        self.manager.current = 'CADASTRO'