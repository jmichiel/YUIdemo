'''
Created on 22-feb-2010

@author: jm
'''
import grok
from megrok import layout
from zope.interface import Interface
from hurry import yui
from zope.interface import alsoProvides

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
    

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
    
class IAJAXLayer(IDefaultBrowserLayer):
    grok.skin('ajax')
    
class AJAXLayout(layout.Layout):
    grok.layer(IAJAXLayer)
    grok.context(Interface)
    template=grok.PageTemplate('<tal:tag tal:replace="structure view/content"/>')
    
from zope.app.publication.interfaces import IBeforeTraverseEvent

@grok.subscribe(grok.Application, IBeforeTraverseEvent)
def handle(obj, event):
    if event.request.getHeader('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        alsoProvides(event.request, IAJAXLayer)