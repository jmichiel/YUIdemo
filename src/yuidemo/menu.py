'''
Created on 22-feb-2010

@author: jm
'''
import grok
from megrok import navigation, pagetemplate
from layout import Scripts, StyleSheets
from zope.interface import Interface
from hurry import yui

class MainMenu(navigation.Menu):
    grok.name('main-menu')
    navigation.submenu('blog-menu', 'Blogs')
    
    def update(self):
        super(MainMenu, self).update()
        yui.menu.need()
        
    id = 'main-menu'
    cssClass='yuimenubar yuimenubarnav'
    cssItemClass='yuimenubaritem'
    cssItemLabelClass='yuimenubaritemlabel'
    

class MenuTemplate(pagetemplate.PageTemplate):
    grok.template('menu')
    pagetemplate.view(navigation.interfaces.IMenu)
    
class ItemTemplate(pagetemplate.PageTemplate):
    grok.template('item')
    pagetemplate.view(navigation.interfaces.IMenuItem)
    
    
class MenuScript(grok.Viewlet):
    grok.viewletmanager(Scripts)
    grok.context(Interface)
    grok.template('script')
    
class MenuStylesheet(grok.Viewlet):
    grok.viewletmanager(StyleSheets)
    grok.context(Interface)
    template = grok.PageTemplate('<link rel="stylesheet" type="text/css" tal:attributes="href context/++resource++yui/menu/assets/skins/sam/menu.css" />')


class BlogMenu(navigation.ContentMenu):
    grok.name('blog-menu')
    
    def update(self):
        super(BlogMenu, self).update()
        yui.menu.need()
        
    def getContent(self):
        return grok.getSite().values()
    def getTitle(self, entry):
        return entry.title

    id = 'blog-menu'
    cssClass='yuimenu yuimenunav'
    cssItemClass='yuimenuitem'
    cssItemLabelClass='yuimenuitemlabel'
