from zope import component
from Products.CMFCore.utils import getToolByName

from plone.registry.interfaces import IRegistry
from plone.registry.record import Record
from plone.registry import field
from collective.galleria import i18n

PROFILE = 'profile-collective.galleria:default'

def upgrade_1020_to_1021(context):
    registry = component.getUtility(IRegistry)
    record = Record(field.Bool(title=i18n.responsive,
                               description=i18n.responsive_desc,),
                    False)
    rid ='collective.galleria.interfaces.settings.IGalleriaSettings.responsive'
    registry.records[rid] = record

def upgrade_1010_to_1020(context):

    site = context.aq_parent
    catalog = getToolByName(site, 'portal_catalog')
    types = ('Folder','Topic','Link')

    for portal_type in types:
        brains = catalog(portal_type=portal_type)

        for brain in brains:
            ob = brain.getObject()
            layout = ob.getLayout()

            if layout == 'galleria.html':
                ob.setLayout('galleria_view')

    setup = getToolByName(site, 'portal_setup')
    setup.runImportStepFromProfile('profile-collective.galleria:default',
                                   'typeinfo', run_dependencies=False,
                                   purge_old=False)


def upgrade_1000_to_1010(context):
    
    context.runImportStepFromProfile(PROFILE, 'browserlayer')
    context.runImportStepFromProfile(PROFILE, 'plone.app.registry')
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')
    jsregistry.unregisterResource('++resource++collective.galleria.classic.js')
    cssregistry.unregisterResource('++resource++collective.galleria.classic.css')
