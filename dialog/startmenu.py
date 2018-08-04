#-*- coding:utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file("kvdialog/startmenu.kv")

class CStartMenu(Screen):
    def on_entergame(self):
        print "on_entergame"

    def on_quitgame(self):
        exit(1)