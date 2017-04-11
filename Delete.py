import pysolr
import id_List


def Delete_desc(file_path):
    core = 'http://localhost:8983/solr/desc'
	core.delete('path:' + file_path)
	find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delate_txt(file_path):
	core = 'http://localhost:8983/solr/txt'
	core.delete('path:' + file_path)
	find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delete_info(file_path):
	core = 'http://localhost:8983/solr/info'
	core.delete('path:' + file_path)
	find_line = [s for s in id_List if s[1] == file_path]
	id_List.Delete_list_path(file_path)

def Delete_id(id_num):
    find_line = [s for s in id_List if s[0] == id_num]
	core = [p[2] for p in id_List if p[0] == id_num]
	core.delete('id:' + id_num)
	id_List.Delete_list_id(id_num)
