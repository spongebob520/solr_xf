import pysolr
import id_List

def Delete_all():
	core_desc = pysolr.Solr('http://localhost:8983/solr/desc')
	core_desc.delete(q='*:*')
	core_txt = pysolr.Solr('http://localhost:8983/solr/txt')
	core_txt.delete(q='*:*')
	core_info = pysolr.Solr('http://localhost:8983/solr/info')
	core_info.delete(q='*:*')
	print 'The index library has been cleaned up !'

def Delete_desc(file_path):
	core = pysolr.Solr('http://localhost:8983/solr/desc')
	core.delete(q='path:"' + file_path + '"')
	# print 'path:"'+file_path+'"'
	# find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delate_txt(file_path):
	core = pysolr.Solr('http://localhost:8983/solr/txt')
	core.delete(q='path:"' + file_path + '"')
	# find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delete_info(file_path):
	core = pysolr.Solr('http://localhost:8983/solr/info')
	core.delete(q='path:"' + file_path +'"')
	# find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delete_id(id_num):
	# find_line = [s for s in id_List if s[0] == id_num]
	with open('id_List.txt') as f:
		http = [p.strip().split('\t')[2] for p in f.readlines() if p.strip().split('\t')[0] == id_num]
		core_http = ''.join(http)
		print core_http
		core = pysolr.Solr(core_http)
		core.delete(id = id_num)
		id_List.Delete_list_id(id_num)
