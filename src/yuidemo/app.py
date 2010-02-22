import grok
from megrok import layout

class Yuidemo(grok.Application, grok.Container):
    pass

class Index(layout.Page):
    pass # see app_templates/index.pt
