#encoding: utf-8

import os
import sys
import pysolr
import id_List
from time import ctime
from multiprocessing.dummy import Pool as ThreadPool
import json
import requests
from time import clock

# txt文档为结构化文档，只有两列和四列的区分，当列数为其他情况时候，不做处理
def add_txt(files_path, core, core_http):
	core.delete(os.path.abspath(files_path))
	id_List.Delete_list_path(files_path)
	dicts = []
	with open(files_path, 'rb') as f:
		for i, line in enumerate(f):
			words = [s.decode('utf-8') for s in line.strip().split()]
			if i == 0:
				if len(words) == 4:
					fields = ('wav', 'start', 'end', 'text', 'path', 'id')
				elif len(words) == 2:
					fields = ('wav', 'text', 'path', 'id')
				else:
					print 'ERROR! ' + files_path + ' is not the correct format!'
					return

			id_num = id_List.Create_id()
			words.extend([os.path.abspath(files_path), id_num])
			dicts.append(dict(zip(fields, words)))
			id_List.Create_list(files_path, id_num, core_http)

        core.add(dicts)


def add_info(files_path, core, core_http):
	core.delete(os.path.abspath(files_path))
	id_List.Delete_list_path(files_path)
	with open(files_path, 'rb') as f:
		dicts = []
		url = 'http://localhost:8983/solr/info/schema'
		text = f.readline()
		words = text.strip().split()
		# print words
		for word in words:
			add_field(url, word)
		fields = [n.decode('utf-8') for n in text.strip().split()]
		# print fields
		fields.extend([u'path', u'content', u'id'])
		# print fields
		for line in f.readlines():
			words = [s.decode('utf-8') for s in line.strip().split()]
			id_num = id_List.Create_id()
			words.extend([os.path.abspath(files_path).decode('utf-8'), line.decode('utf-8'), id_num])
			dicts.append(dict(zip(fields, words)))
			id_List.Create_list(files_path, id_num, core_http)
        core.add(dicts)

def add_desc(files_path, core, core_http):
	id_List.Delete_list_path(files_path)
	with open(files_path, 'rb') as f:
		text = f.read().decode('utf-8')
		id_num = id_List.Create_desc_id(files_path)
		core.add([{'id': id_num,
                           'path': os.path.abspath(files_path),
		           'context': text}])
		id_List.Create_list(files_path, id_num, core_http)

def add_wrapper(files_path):
	total_http = 'http://localhost:8983/solr/all'
	core_total = pysolr.Solr(total_http)
	postfix = files_path.split('.')[-1]
	if postfix == 'desc':
		core_http = 'http://localhost:8983/solr/desc'
		core = pysolr.Solr(core_http)
		add_desc(files_path, core, core_http)
		add_desc(files_path, core_total, total_http)
	elif postfix == 'txt':
		core_http = 'http://localhost:8983/solr/txt'
		core = pysolr.Solr(core_http)
		add_txt(files_path, core, core_http)
		add_txt(files_path, core_total, total_http)
	elif postfix == 'info':
		core_http = 'http://localhost:8983/solr/info'
		core = pysolr.Solr(core_http)
		add_info(files_path, core, core_http)
		add_info(files_path, core_total, total_http)

'''
def add_all(files_path, core, core_http):
	add_desc(files_path, core, core_http)
	add_txt(files_path, core, core_http)
	add_info(files_path, core, core_http)
'''	

def SearchForFiles(Home_dir):
	for path, folder, files in os.walk(Home_dir):
		task_pool = ThreadPool(8)
		files_path=[os.path.join(path, f) for f in files]
		print files_path
		task_pool.map(add_wrapper, files_path)
		task_pool.close()
		task_pool.join()

# info文件的表头是中文，读取info文件时候直接用表头做field名称会出现乱码，这里根据表头采用手动添加field
def add_field(url, field):
        data = json.dumps({'add-field': {'name': field, 'type': 'strings'}})
        reponse = requests.post(url=url, data=data)


if __name__ == '__main__':                    
    # url = 'http://10.20.0.71:8983/solr/gettingstarted/update'
    Home_dir = sys.argv[1]
    start_time = clock()
    SearchForFiles(Home_dir)
    end_time = clock()
    print 'Establish index finished, total time:', end_time - start_time

