# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'dnd.mobile.languages.views',

    # languages
    url(
        r'^$',
        'language_index_mobile',
        name='language_index_mobile'
    ),
    # languages > detail
    url(
        r'^(?P<language_slug>[^/]+)/$',
        'language_detail_mobile',
        name='language_detail_mobile'
    ),
)
