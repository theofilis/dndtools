# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'dnd.mobile.deities.views',

    # deities
    url(
        r'^$',
        'deity_list_mobile',
        name='deity_list_mobile',
    ),
    # deities > detail
    url(
        r'^(?P<deity_slug>[^/]+)/$',
        'deity_detail_mobile',
        name='deity_detail_mobile',
    ),
)
