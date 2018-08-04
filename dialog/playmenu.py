#-*- coding:utf-8 -*-
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

Builder.load_file("kvdialog/playmenu.kv")

class CBoxContainer(FloatLayout):
    pass
    
class CPlayMenu(Screen):
    m_BoxContainer = ObjectProperty()
    def __init__(self, **kwargs):
        super(CPlayMenu, self).__init__(**kwargs)
        self.m_BoxManager = None

    def buildboxs(self):
        self.m_BoxContainer.clear_widgets()