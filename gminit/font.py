#-*- coding:utf-8 -*-
#字体初始化

import os
import define
from kivy.resources import(
    resource_add_path,
    resource_find,
)

from kivy.core.text import LabelBase

def Init():
    resource_add_path(os.path.abspath("./resource"))

    LabelBase.register(define.FONT_COMMON, "./font/simkai.ttf")
    LabelBase.register(define.FONT_HEI, "./font/simhei.ttf")


