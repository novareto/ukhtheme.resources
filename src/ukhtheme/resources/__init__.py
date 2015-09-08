# -*- coding: utf-8 -*-

import logging
from os import path
from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('ukhtheme.resources', 'static')

table = Resource(library, 'table.css')
jbs = Resource(library, 'jasny-bootstrap.js', depends=[jquery])
cbs = Resource(library, 'jasny-bootstrap.css')

bootstrap_css = Resource(
    library, 'bootstrap_bundle.css', compiler='less',
    source='bootstrap_bundle.less')

siguv_css = Resource(
    library, 'siguv.css', compiler='less',
    source='siguv.less')

maincss = Resource(library, 'main.css', depends=[bootstrap_css, siguv_css])
mainjs = Resource(library, 'main.js', bottom=True)
#siguvcss = Resource(library, 'ukhtheme.css')
tune = Group([maincss, cbs, jbs, mainjs])

datepicker_css = Resource(
    library, path.join('datepicker', 'bootstrap-datepicker.css'))

datepicker = Resource(
    library, path.join('datepicker', 'bootstrap-datepicker.js'),
    depends=[datepicker_css, tune])

datepicker_de = Resource(
    library, path.join('datepicker', 'locales', 'bootstrap-datepicker.de.js'),
    depends=[datepicker])

datepicker_fr = Resource(
    library, path.join('datepicker', 'locales', 'bootstrap-datepicker.fr.js'),
    depends=[datepicker])

all_dates = Resource(library, 'dates.js', bottom=True, depends=[datepicker])

logger = logging.getLogger('uvcsite.bg.ukhtheme')


def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
