'''
Created on 22-feb-2010

@author: jm
'''
import grok
from megrok import layout
from zope.interface import Interface
from hurry import yui

grok.templatedir('app_templates')

class Layout(layout.Layout):
    grok.context(Interface)
    
    def update(self):
        yui.reset_fonts_grids.need()
        yui.base.need()


class Scripts(grok.ViewletManager):
    grok.context(Interface)
    
class StyleSheets(grok.ViewletManager):
    grok.context(Interface)