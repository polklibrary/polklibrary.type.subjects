from plone import api
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.registry.interfaces import IRegistry
from plone.supermodel import model
from zope import schema
from zope.component import queryUtility
from zope.component import getUtility
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

def discipline_list(context):
    voc = []
    try:
        registry = queryUtility(IRegistry)
        if registry:
            record = registry.get('polklibrary.type.subjects.disciplines', ())
            for v in record:
                voc.append(SimpleTerm(value=v, title=v))
            return SimpleVocabulary(voc)
        return SimpleVocabulary([])
    except Exception as e:
        return SimpleVocabulary([])
directlyProvides(discipline_list, IContextSourceBinder)


class ISubject(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=False,
        )
        
    body = RichText(
            title=u"Body",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
                
    disciplines = schema.List(
            title=u"Disciplines in this subject.",
            description=u"Used to create key legend.",
            required=False,
            value_type=schema.Choice(source=discipline_list),
        )
        
                
    exclude_from_nav = schema.Bool(
            title=u"Exclude from navigation",
            description=u"",
            required=False,
            default=False,
        )
        
        
@indexer(ISubject)
def make_searchable(object, **kwargs):
    import re
    portal_transforms = api.portal.get_tool(name='portal_transforms')
    data = portal_transforms.convertTo('text/plain', object.body.output, mimetype='text/structured')
    text = data.getData()
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', object.body.output)
    return [object.title, object.description, text] + urls
        
        
        
        
        