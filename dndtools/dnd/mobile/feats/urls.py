# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'dnd.mobile.feats.views',


    # feats
    url(
        r'^$',
        'feat_index_mobile',
        name='feat_index_mobile',
    ),
    #feats > categories
    url(
        r'^categories/$',
        'feat_category_list_mobile',
        name='feat_category_list_mobile',
    ),
    #feats > categories > category
    url(
        r'^categories/(?P<category_slug>[^/]+)/$',
        'feat_category_detail_mobile',
        name='feat_category_detail_mobile',
    ),
    # feats > rulebook
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/$',
        'feats_in_rulebook_mobile',
        name='feats_in_rulebook_mobile',
    ),
    # feats > rulebook > feat
    url(
        r'^(?P<rulebook_slug>[^/]+)--(?P<rulebook_id>\d+)/(?P<feat_slug>[^/]+)--(?P<feat_id>\d+)/$',
        'feat_detail_mobile',
        name='feat_detail_mobile',
    ),
)
