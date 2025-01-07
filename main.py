from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from App.Tela_Login.TelaLogin import TelaLoginView
from App.Tela_Princ.TelaPrinc import TelaPrincView
from App.Pokemon.Pokemon import PokemonView
from App.RickandMorty.RickandMorty import RickandMortyView


class MyApp(MDApp):

    title = 'H G TECH'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        Window.size = (400, 650)
        self.load_all_kv_files(self.directory)
        self.sm = ScreenManager()
        
    def build(self):
            
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.accent_palette = 'Orange'
        self.theme_cls.accent_hue = '900'
        self.theme_cls.material_style = "M2"

        #self.sm.add_widget(TelaLoginView())
        self.sm.add_widget(TelaPrincView())
        self.sm.add_widget(PokemonView())
        self.sm.add_widget(RickandMortyView())


        return self.sm
    
MyApp().run()
