# -*- coding: utf-8 -*-
import json
from zope import component
from zope import interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.configviews import ConfigurableBaseView

from collective.galleria import i18n

transitions = SimpleVocabulary(
    [SimpleTerm(value='fade', title=i18n.fade),
     SimpleTerm(value='flash', title=i18n.flash),
     SimpleTerm(value='pulse', title=i18n.pulse),
     SimpleTerm(value='slide', title=i18n.slide),
     SimpleTerm(value='fadeslide', title=i18n.fadeslide)])

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


    showInfo = schema.Bool(title=i18n.showInfo,
                          description=i18n.showInfo_desc,
                          default=True)
    
    _toggleInfo = schema.Bool(title=i18n.toggleInfo,
                              description=i18n.toggleInfo_desc,
                              default=True)

    showCounter = schema.Bool(title=i18n.showCounter,
                          description=i18n.showCounter_desc,
                          default=True)

    showImagenav = schema.Bool(title=i18n.showImagenav,
                          description=i18n.showImagenav_desc,
                          default=True)


    transition = schema.Choice(title=i18n.transition,
                          description=i18n.transition_desc,
                          default='fade',
                          vocabulary=transitions)

    transitionSpeed = schema.Int(title=i18n.transitionSpeed,
                        default=400)

    pauseOnInteraction = schema.Bool(title=i18n.pauseOnInteraction,
                          description=i18n.pauseOnInteraction_desc,
                          default=True)

    width = schema.ASCIILine(title=i18n.width,
                           description=i18n.width_desc,
                           default='550')

    height = schema.Int(title=i18n.height,
                        default=320)

    debug = schema.Bool(title=i18n.debug,
                        description=i18n.debug_desc,
                        default=False)

class Galleria(ConfigurableBaseView):
    settings_schema = IGalleriaSettings
    jsvarname = 'galleriaconfig'
    settings_providers = ('context.zope.annotation',)
    jsdata = 'galleriedata'
#
#    def gallery_data(self):
#        gallery = component.getMultiAdapter((self.context, self.request),
#                                            name="gallery")
#        photos = gallery.photos()
#        data = []
#        for photo in photos:
#            info = {'thumb': photo.thumb_url,
#                    'image': photo.url,
#                    'title': photo.title,
#                    'description': photo.descripiton}
#                    #link: 'http://my.destination.com
#            data.append(info)
#        return self.jsdata + '= ' + json.dumps(data)
