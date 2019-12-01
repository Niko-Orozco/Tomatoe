#!/usr/bin/env python3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_string('''
<TakePicture>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'capture'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class TakePicture(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("./photo/t.png")
        print("Captured")


class MiCamara(App):
    def build(self):
        return TakePicture()

if __name__ == '__main__':
    MiCamara().run()
