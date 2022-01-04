from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from googletrans import Translator

def Translate(info1,lang):
    t = Translator()
    result = t.translate(info1,dest=lang).text
    return result

class Box1(BoxLayout):
    inp = ObjectProperty(None)
    out = ObjectProperty(None)
    spin = ObjectProperty(None)
    def pressed(self):
        self.out.text = Translate(self.inp.text,self.ids.spin.text)
    def clicked(self,value):
        self.spin.text = value

class TranslationApp(App):
    def build(self):
        return Box1()

TranslationApp().run()