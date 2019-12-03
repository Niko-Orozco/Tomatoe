#!/usr/bin/env python3
import sys
sys.path.append('../')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
#from Model import predict as pred
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_file('./design.kv')

class MyScreenManager(ScreenManager):
    def __init__(self):
        super(MyScreenManager, self).__init__()


class VentanaMenu(Screen):
    pass


class VentanaNuevas(Screen, BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("./photo/t.png")
        print("Captured")


class VentanaTanda(Screen):
    def showanswer(self):
        self.ids['label2'].text = "filetext"


class RunApp(App):
    def build(self):
        return MyScreenManager()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ in ('__main__', '__android__'):
    RunApp().run()
