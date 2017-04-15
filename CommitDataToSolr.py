#encoding: utf-8

import os
import pysolr
import id_List


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
		fields = [n.decode('utf-8') for n in f.readline().strip().split()]
		fields.extend([u'path', u'content', u'id'])
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
				   'context': text
				 }])
		id_List.Create_list(files_path, id_num, core_http)

def SearchForFiles(Home_dir):
    for path, folder, files in os.walk(Home_dir):
        for filename in files:
            files_path=os.path.join(path, filename)
            print files_path
            postfix = filename.split('.')[-1]

            if postfix == 'desc':
				core_http = 'http://localhost:8983/solr/desc' 
				core = pysolr.Solr(core_http)
				add_desc(files_path, core, core_http)
            elif postfix == 'txt':
				core_http = 'http://localhost:8983/solr/txt'
				core = pysolr.Solr(core_http)
				add_txt(files_path, core, core_http)
            elif postfix == 'info':
				core_http = 'http://localhost:8983/solr/info'
				core = pysolr.Solr(core_http)
				add_info(files_path, core, core_http)


if __name__ == '__main__':
    # url = 'http://10.20.0.71:8983/solr/gettingstarted/update'
    Home_dir = os.getcwd()
    current_path = os.getcwd()
    print Home_dir
    print current_path 
    SearchForFiles(Home_dir,current_path)

