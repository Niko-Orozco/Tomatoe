#!/usr/bin/env python3
import sys
sys.path.append('../')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from Model import camara as cam
from Model import predict as pred

kv='''
<Botones>
    spacing: 10
    padding: 10
    rows:6
    id: menu

    BoxLayout:
        id: carga
        Button:
            text:'Tomar Foto'
            font_size: 14
            on_press: root.Capture()
        Button:
            center: self.parent.center
            font_size: 14
            height: 28
            background_color: (1.1, 1.0, 0.1, 1.1)
            text:'Consultar estado'
            font_size: 14
            on_press: root.Predict()
'''

class Botones(GridLayout):
    def __init__(self):
        super(Botones, self).__init__()

    def Capture(self):
        cam.RunCam()

    def Predict(self):
        pred.predicts("./Model/photo/t.png")

class Menu(App):
    def build(self):
        Builder.load_string(kv)
        return Botones()


def Startup():
    Menu().run()
