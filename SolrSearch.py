#!/usr/bin/python
# -*- coding: utf-8 -*-

import pysolr

solr = pysolr.Solr('http://10.20.0.71:8983/solr/' + 'gettingstarted_shard1_replica2')

#'xufei'处的字段为想要查询的内容
results = solr.search('xufei', **{
    'rows': 10,
    'hl': 'true',
    'hl.simple.pre': '<em class="hlt1">',
    'hl.simple.post': '</em>',
    "hl.fl": "article_title",
})

print results.hits

print results.docs

print results.highlighting
