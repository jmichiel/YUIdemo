import grok
from megrok import layout

from megrok import navigation
from menu import MainMenu

class Yuidemo(grok.Application, grok.Container):
    pass

class Index(layout.Page):
    navigation.sitemenuitem(MainMenu, 'Home', order=-1)
