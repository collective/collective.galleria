from Products.CMFCore.utils import getToolByName

PROFILE = 'profile-collective.galleria:default'

def upgrade(context):
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
