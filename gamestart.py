#-*- coding:utf-8 -*-
import define
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from dialog import startmenu

class CScreenManager(ScreenManager):
    pass

class C2048App(App):
    def build(self):
        sm = ScreenManager()
        
        oMenu = startmenu.CStartMenu(name=define.START_MENU)
        sm.switch_to(oMenu)
        return sm

def Start():
    C2048App().run()