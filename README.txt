Introduction
============

Galleria_ is a great JQuery slideshow plugin. This integration
is based on collective.gallery and provide most of galleria options
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

width
-----

By default, Galleria fetches the width from the containing element. Bu you can use this option to set a gallery width manually.

height
------

Galleria need a height to work properly. You can set the height using this option to make sure it has the correct height.
If no height is set, Galleria will try to find the height of the parent container.

debug
-----

This option is for turning debug on/off. By default, Galleria
displays errors by printing them out in the gallery container and
sometimes throw exceptions. For deployment you can turn debug off
to generate a more generic error message if a fatal error is raised.

Notes
=====

Galleria in its way to manage theme parse all link tags to find the css attached
to the theme. To make it work in production mode you must add themes javascript
and css called by the template. 
::

    // look for manually added CSS
    $('link').each(function( i, link ) {
        reg = new RegExp( theme.css.replace('\+\+resource\+\+','\\+\\+resource\\+\\+') );
        if ( reg.test( link.href ) ) {
            // we found the css
            css = true;
            Galleria.theme = theme;
            return false;
        }
    });

As you can see the original code has been patched to support ++resource++ url.


Credits
=======

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

Authors

  - JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

Contributors

  -

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _galleria: http://galleria.aino.se
 
