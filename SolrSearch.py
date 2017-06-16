#!/usr/bin/python
# -*- coding: utf-8 -*-

import xfsolr


def SolrSearch(types, key_word):
	core = xfsolr.Solr('http://10.20.0.71:8983/solr/' + types)

	#'xufei'处的字段为想要查询的内容
	results = core.search(key_word.decode('utf-8'), **{
					      'hl': 'true',
				              'hl.fragsize': 10,
                                              })

	print results.hits

	# print results.docs

	# print results.highlighting
