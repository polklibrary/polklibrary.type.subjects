from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import json

class SubjectsView(BrowserView):

    template = ViewPageTemplateFile("subject.pt")
    
    def __call__(self):
        return self.template()
        
    def get_disciplines(self):
        result = {}
        for i in self.context.disciplines:
            result[i] = i
        return json.dumps(result)

    @property
    def portal(self):
        return api.portal.get()
