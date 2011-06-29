# -*- coding: utf-8 -*-
import json
from zope import component
from zope import interface
from zope import schema
from collective.configviews import ConfigurableBaseView

from collective.galleria import i18n

class IGalleriaSettings(interface.Interface):
    """http://galleria.aino.se/docs/1.2/options/
    """

    autoplay   = schema.Bool(title=i18n.autoplay,
                             description=i18n.autoplay_desc,
                             default=True)
    carousel   = schema.Bool(title=i18n.carousel,
                             description=i18n.carousel_desc,
                             default=True)
    carouselFollow = schema.Bool(title=i18n.carouselFollow,
                                 description=i18n.carouselFollow_desc,
                                 default=True)

    width = schema.ASCIILine(title=i18n.width,
                           description=i18n.width_desc,
                           default='auto')

class Galleria(ConfigurableBaseView):
    settings_schema = IGalleriaSettings
    jsvarname = 'galleriaconfig'
    settings_providers = ('context.zope.annotation',)
    jsdata = 'galleriedata'

    def gallery_data(self):
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
