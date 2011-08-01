from zope.i18nmessageid import MessageFactory

_ = messageFactory = MessageFactory('collective.tinyslideshow')

autoplay = _(u"autoplay",default=u"auto play")
autoplay_desc_default=u"""If true, this will start playing the slideshow with
                 5 seconds interval (default). If you set this to any number,
                 f.ex 4000, it will start playing with that interval 
                 (in milliseconds)"""
autoplay_desc = _(u"autoplay_desc",default=autoplay_desc_default)
carousel = _(u"carousel",default=u"carousel")
carousel_desc_default=u"""Galleria comes with a built-in horizontal carousel.
                        This options is for activating / deactivating the
                        carousel feature. Setting this to true, the carousel
                        will be automatically applied if the total som of
                        thumbnails width exceeds the thumbnail container.
                        This will be re-calculaed on resize.

                        If you set this to false, you will prevent Galleria
                        from adding the carousel."""
carousel_desc = _(u"carousel_desc",default=carousel_desc_default)

carouselFollow = _(u"carouselFollow",
                   default=u"carousel follow")
carouselFollow_desc = _(u"carouseilFollow_desc",
                        default=u"""This option defines if the the carousel 
                        should follow the active image. You can control the
                        speed of the animation with the carouselSpeed option.
                        Please note that animating heavy thumbnails can affect
                        your main image animation, so if you are seeing big 
                        lags in the main animation you can try to set this
                        option to false.""")

showInfo = _(u"showInfo",default=u"show Info")
showInfo_default = u"""Set this to false if you do not wish to display the
                       caption."""
showInfo_desc =_(u"showInfo_desc", default=showInfo_default)

showCounter = _(u"showCounter", default=u"show Counter")
showCounter_default=u"""Set this to false if you do not wish to display the
                        counter."""
showCounter_desc = _(u"showCounter_desc", default=showCounter_default)

showImagenav = _(u"showImagenav", default=u"show Imagenav")
showImagenav_default=u"""Set this to false if you do not wish to display the
                         image navigation (next/prev arrows)."""
showImagenav_desc = _(u"showImagenav_desc", default=showImagenav_default)

transition = _(u"transition", default=u"transition")
transition_default=u"""The transition that is used when displaying the images.
                There are some built-in transitions in Galleria, but you can
                also create your own using our Transitions API."""
transition_desc = _(u"transition_desc", default=transition_default)

debug = _(u"debug", default=u"Debug")
debug_default=u"""This option is for turning debug on/off. By default, Galleria
            displays errors by printing them out in the gallery container and
            sometimes throw exceptions. For deployment you can turn debug off
            to generate a more generic error message if a fatal error is
            raised."""
debug_desc = _(u"debug_desc", default=debug_default)

pauseOnInteraction = _(u"pauseOnInteraction", default=u"pause on interaction")
pauseOnInteraction_default=u"""During playback, Galleria will stop the playback
            if the user presses thumbnails or any other navigational links.
            If you dont want this behaviour, set this option to false."""
pauseOnInteraction_desc = _(u"pauseOnInteraction_desc",
                            default=pauseOnInteraction_default)

transitionSpeed = _(u"transitionSpeed", default=u"Transition speed")
transitionSpeed_default=u"""The milliseconds used in the animation when applying
            the transition. The higher number, the slower transition."""
transitionSpeed_desc = _(u"transitionSpeed_desc", default=transitionSpeed_default)

toggleInfo = _(u"toggleInfo", default=u"toggleInfo")
toggleInfo_default=u"""Set this to false if you want to show the caption
                       all the time:"""
toggleInfo_desc = _(u"toggleInfo_desc", default=toggleInfo_default)

# = _(u"", default=u"")
#_default=u""" """
#_desc = _(u"_desc", default=_default)

# = _(u"", default=u"")
#_default=u""" """
#_desc = _(u"_desc", default=_default)
#
# = _(u"", default=u"")
#_default=u""" """
#_desc = _(u"_desc", default=_default)

# = _(u"", default=u"")
#_default=u""" """
#_desc = _(u"_desc", default=_default)
#
# = _(u"", default=u"")
#_default=u""" """
#_desc = _(u"_desc", default=_default)

width = _(u"width",default="Width")
width_desc = _(u"width_desc",
               default=u"""By default, Galleria fetches the width from the
               containing element. Bu you can use this option to set a gallery
               width manually.""")

height = _(u"height",default="Height")
height_desc = _(u"height_desc",
              default=u"""Galleria need a height to work properly. You can set
              the height using this option to make sure it has the correct
              height. If no height is set, Galleria will try to find the height
              of the parent container.""")

#vocabulary
fade = _(u'Fade')
flash= _(u'Flash')
pulse = _(u'Pulse')
slide = _(u'Slide')
fadeslide = _(u'Fade slide')
