from kivymd.uix.screen import MDScreen


class TelaLoginView(MDScreen):
    def login (self):

        usuario = 'admin'
        senha = 'admin'

        if self.ids.usuario.text == usuario and self.ids.senha.text == senha:
            
            self.manager.transition.direction = 'left'
            self.manager.current = 'princ_view'
            self.ids.erro.text = ''
        else:
            self.ids.erro.text = 'Usuário ou Senha Incorreto!'