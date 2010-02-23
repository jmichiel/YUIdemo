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

grok.templatedir('app_templates')

class IBlogEntry(Interface):
    title = schema.TextLine(title=u'title')
    text = schema.Text(title=u'Body')
    
class BlogEntry(grok.Model):
    grok.implements(IBlogEntry)
    
class BlogIndex(layout.Page):
    grok.name('index')
    
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