import grok

class Yuidemo(grok.Application, grok.Container):
    pass

class Index(grok.View):
    pass # see app_templates/index.pt
