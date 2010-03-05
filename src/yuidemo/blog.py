'''
Created on 23-feb-2010

@author: jm
'''
import grok
from zope.interface import Interface
from zope import schema
from megrok import layout, navigation
from urllib import quote_plus
from menu import BlogMenu, ActionMenu
from megrok import resource
from hurry import yui
from layout import Scripts, StyleSheets
from cgi import escape
from message import flash

class IBlogEntry(Interface):
    title = schema.TextLine(title=u'title')
    text = schema.Text(title=u'Body')

    
class BlogEntry(grok.Model):
    grok.implements(IBlogEntry)

    @property
    def htmltext(self):
        return escape(self.text).replace('\n', '<br/>');
    
class BlogIndex(layout.Page):
    grok.name('index')
    resource.include(yui.tabview)
    resource.include(yui.connection)
    
class BlogView(layout.Page):
    navigation.menuitem(ActionMenu, 'View', order=-1)
    grok.name('view')
    
class MetaDataView(layout.Page):
    navigation.menuitem(ActionMenu, 'Meta Data', order=-1)
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
        flash("New blog entry '%s' added!" % entry.title, type='blog')
        self.redirect(self.url(entry))

class Edit(layout.EditForm):
    navigation.menuitem(ActionMenu, 'Edit', order=-1)
    grok.context(IBlogEntry)
    form_fields = grok.Fields(IBlogEntry)
    
    @grok.action('Save Entry')
    def Save(self, **data):
        self.applyData(self.context, **data)
        flash("Blog entry '%s' updated!" % self.context.title, type='blog')
        self.redirect(self.url(self.context, 'view'))
        
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
