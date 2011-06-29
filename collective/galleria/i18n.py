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

width = _(u"width",default="Width")
width_desc = _(u"width_desc",
               default=u"""By default, Galleria fetches the width from the containing element. Bu you can use this option to set a gallery width manually.""")
