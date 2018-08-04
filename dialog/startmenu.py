#-*- coding:utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import define

Builder.load_file("kvdialog/startmenu.kv")

class CStartMenu(Screen):
    def on_entergame(self):
        import playmenu

        if not self.manager.has_screen(define.PLAY_MENU):
            oPlayMenu = playmenu.CPlayMenu(name=define.PLAY_MENU)
        else:
            oPlayMenu = self.manager.get_screen(define.PLAY_MENU)
        
        print "switch_to menu:", oPlayMenu
        self.manager.switch_to(oPlayMenu)
            

    def on_quitgame(self):
        exit(1)