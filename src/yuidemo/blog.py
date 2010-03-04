'''
Created on 23-feb-2010

@author: jm
'''
import grok
from zope.interface import Interface
from zope import schema
from megrok import layout, navigation
from urllib import quote_plus
from menu import BlogMenu
from megrok import resource
from hurry import yui
from layout import Scripts, StyleSheets


class IBlogEntry(Interface):
    title = schema.TextLine(title=u'title')
    text = schema.Text(title=u'Body')
    
class BlogEntry(grok.Model):
    grok.implements(IBlogEntry)
    
class BlogIndex(layout.Page):
    grok.name('index')
    resource.include(yui.tabview)
    resource.include(yui.connection)
    
class BlogView(grok.View):
    grok.name('view')
    
class MetaDataView(grok.View):
    grok.name('meta')

class Add(layout.AddForm):
    navigation.sitemenuitem(BlogMenu, order=-1)
    grok.title('Add a Blog Entry')
    grok.context(grok.Application)
    form_fields = grok.Fields(IBlogEntry)
    
    @grok.action('Add entry')
    def Add(self, **data):
        entry = BlogEntry()
        self.applyData(entry, **data)
        grok.getSite()[quote_plus(entry.title)] = entry
        self.redirect(self.url(entry))
        
class BlogIndexScript(grok.Viewlet):
    grok.view(BlogIndex)
    grok.viewletmanager(Scripts)
    grok.context(Interface)
    grok.template('script')
    

class BlogIndexStylesheet(grok.Viewlet):
    grok.viewletmanager(StyleSheets)
    grok.context(Interface)
    template = grok.PageTemplate('<link rel="stylesheet" type="text/css" '
                                 'tal:attributes="href context/++resource++yui/tabview/assets/skins/sam/tabview.css" />')
