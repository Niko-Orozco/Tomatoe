#!/usr/bin/env python3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kv='''
<MyWidget>
    spacing: 10
    padding: 10
    rows:6
    id: registro

    BoxLayout:
        id: cedula
        Label:
            text:'Cédula'
            font_size: 16
        TextInput:
            id: key
            multiline:False
    BoxLayout:
        id: nombre
        Label:
            text:'Nombre y Apellido'
            font_size: 16
        TextInput:
            multiline:False
    BoxLayout:
        id: Correo
        Label:
            text:'Correo Electrónico'
            font_size: 16
        TextInput:
            id: mail
            multiline:False
    BoxLayout:
        id: carga
        Button:
            text:'Registrar'
            font_size: 14
            on_press: root.reg()
        Button:
            text:'Cancelar'
            font_size: 14
'''

class MyWidget(GridLayout):
    def __init__(self):
        super(MyWidget, self).__init__()

    def reg(self):
        print ('El botón si llama la función')

class registroApp(App):
    def build(self):
        Builder.load_string(kv)
        return MyWidget()

if __name__ == '__main__':
    registroApp().run()
