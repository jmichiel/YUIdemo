'''
Created on 4-mrt-2010

@author: jm
'''
import grok
from zope.interface import Interface
from hurry import yui
from layout import StyleSheets, Scripts
from zope import component
from z3c.flashmessage.interfaces import IMessageReceiver, IMessageSource


def flash( message, type='message'):
    source = component.getUtility(IMessageSource, name='session')
    source.send(message, type)

class MessagesScript(grok.Viewlet):
    grok.viewletmanager(Scripts)
    grok.context(Interface)
    grok.template('script')
    
    def update(self):
        yui.container.need()
        yui.dragdrop.need()
        yui.json.need()
        
    @property
    def messageurl(self):
        return self.view.url(grok.getSite(), 'messages')
    
class PanelStylesheet(grok.Viewlet):
    grok.viewletmanager(StyleSheets)
    grok.context(Interface)
    template = grok.PageTemplate('<link rel="stylesheet" type="text/css" '
            'tal:attributes="href '
            'context/++resource++yui/container/assets/skins/sam/container.css" />')

class JSONMessages(grok.JSON):
    grok.context(grok.Application)
    
    def messages(self):
        receiver = component.getUtility(IMessageReceiver)
        return [{'message':m.message, 'type':m.type} for m in receiver.receive()]
    