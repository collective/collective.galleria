from Products.CMFCore.utils import getToolByName

PROFILE = 'profile-collective.galleria:default'

def upgrade(context):
    
    context.runImportStepFromProfile(PROFILE, 'browserlayer')
    context.runImportStepFromProfile(PROFILE, 'plone.app.registry')
    jsregistry = getToolByName(context, 'portal_javascripts')
    cssregistry = getToolByName(context, 'portal_css')
    jsregistry.unregisterResource('++resource++collective.galleria.classic.js')
    cssregistry.unregisterResource('++resource++collective.galleria.classic.css')
