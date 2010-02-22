'''
Created on 22-feb-2010

@author: jm
'''
import grok
from megrok import navigation
from megrok import pagetemplate

class MainMenu(navigation.Menu):
    grok.name('main-menu')
    
    cssClass='yuimenubar yuimenubarnav'
    cssItemClass='yuimenubaritem'
    cssItemLabelClass='yuimenubaritemlabel'
    

class MenuTemplate(pagetemplate.PageTemplate):
    grok.template('menu')
    pagetemplate.view(navigation.interfaces.IMenu)
    
class ItemTemplate(pagetemplate.PageTemplate):
    grok.template('item')
    pagetemplate.view(navigation.interfaces.IMenuItem)