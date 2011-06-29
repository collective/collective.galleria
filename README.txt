Introduction
============

Galleria_ is a great JQuery slideshow plugin. This integration
is based on collective.gallery and provide most of galleria option
throw collective.configviews

Options
=======

autoplay
--------

If true, this will start playing the slideshow with
5 seconds interval (default). If you set this to any number,
f.ex 4000, it will start playing with that interval 
(in milliseconds)

carousel
--------

Galleria comes with a built-in horizontal carousel.
This options is for activating / deactivating the
carousel feature. Setting this to true, the carousel
will be automatically applied if the total som of
thumbnails width exceeds the thumbnail container.
This will be re-calculaed on resize.

If you set this to false, you will prevent Galleria
from adding the carousel.

carouselFollow
--------------

This option defines if the the carousel 
should follow the active image. You can control the
speed of the animation with the carouselSpeed option.
Please note that animating heavy thumbnails can affect
your main image animation, so if you are seeing big 
lags in the main animation you can try to set this
option to false.

showInfo
--------

Set this to false if you do not wish to display the caption.

showCounter
-----------

Set this to false if you do not wish to display the counter.

showImagenav
------------

Set this to false if you do not wish to display the image navigation (next/prev arrows).

transition
----------

The transition that is used when displaying the images.
There are some built-in transitions in Galleria, but you can
also create your own using our Transitions API.

transitionSpeed
---------------

The milliseconds used in the animation when applying
the transition. The higher number, the slower transition.

pauseOnInteraction
------------------

During playback, Galleria will stop the playback
if the user presses thumbnails or any other navigational links.
If you dont want this behaviour, set this option to false.

height
------

debug
-----

This option is for turning debug on/off. By default, Galleria
displays errors by printing them out in the gallery container and
sometimes throw exceptions. For deployment you can turn debug off
to generate a more generic error message if a fatal error is raised.
