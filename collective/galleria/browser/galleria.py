# -*- coding: utf-8 -*-
import json
from zope import component
from collective.configviews import ConfigurableBaseView

from collective.galleria import interfaces

class Galleria(ConfigurableBaseView):
    settings_schema = interfaces.IGalleriaSettings
    jsvarname = 'galleriaconfig'
    settings_providers = ('site.plone.app.registry','context.zope.annotation')
    jsdata = 'galleriadata'

    def gallery_data(self):
        """If you prefer using the json data version, call this method
        in the template"""
        gallery = component.getMultiAdapter((self.context, self.request),
                                            name="gallery")
        photos = gallery.photos()
        data = []
        for photo in photos:
            info = {'thumb': photo.thumb_url,
                    'image': photo.url,
                    'title': photo.title,
                    'description': photo.descripiton}
                    #link: 'http://my.destination.com
            data.append(info)
        return self.jsdata + '= ' + json.dumps(data)

    def portal_url(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                                 name="plone_portal_state")
        return portal_state.portal_url()

    @property
    def settings(self):
        #override settings to support _toggleInfo that is not supported by
        #plone.app.registry
        settings = super(Galleria, self).settings
        settings['_toggleInfo'] = settings['toggleInfo']
        if settings['width'] == 0 :
            #set to 100%
            del settings['width']
        return settings
