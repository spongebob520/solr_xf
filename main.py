# encoding: utf-8
import os
import pysolr
import SolrSearch
import CommitDataToSolr
import Delete
import sys
import id_List

def Delete_index():
	print 'please choose ID NUMBER or ABSOLUTE PATH to delete'
	print 'input', '\033[1;31;40mid', '\033[0mor', '\033[1;31;40mpath', '\033[0mor', '\033[1;31;40mall', '\033[0m:'
	order = raw_input()
	if order == 'id':
		'''
		core_desc = pysolr.Solr('http://localhost:8983/solr/desc')
		core_txt = pysolr.Solr('http://localhost:8983/solr/txt')
		core_info = pysolr.Solr('http://localhost:8983/solr/info')
		'''
		print 'please input the id number below:'
		id_num = raw_input()
		Delete.Delete_id(id_num)
		'''
		core_desc.delete(id = id_num)
		core_txt.delete(id = id_num)
		core_info.delete(id = id_num)
		id_List.Delete_list_id(id_num)
		'''
	elif order == 'path':
	# 删除一个文件路径所创建的所有索引，适用于整个文件被删除的情况
		Check_Exists()

	elif order == 'all':
		Delete.Delete_all()



def Check_Exists():
	print 'Please input the absolute path of the file you want to delete:'
	absolute_path = raw_input()
	# check whether the path exists
	if not os.path.exists(absolute_path):
		print 'the path does not exists'
		sys.exit(-1)
	elif os.path.isfile(absolute_path):
		suffix = absolute_path.split('.')[-1]
		if suffix == 'desc':
			Delete.Delete_desc(absolute_path)
		elif suffix == 'txt':
		    Delete.Delete_txt(absolute_path)
		elif suffix == 'info':
		    Delete.Delete_info(absolute_path)
			

def Add():
	print 'Please input the absolute path of the file you want to add:' 
	absolute_path = raw_input()

	if not os.path.exists(absolute_path):
		print 'ERROR!!!the path does not exists!'
		sys.exit(-1)
	elif os.path.isfile(absolute_path):
		suffix = absolute_path.split('.')[-1]
		if suffix == 'desc':
			core_http = 'http://localhost:8983/solr/desc'
			core = pysolr.Solr(core_http)
			CommitDataToSolr.add_desc(absolute_path, core, core_http)
		elif suffix == 'txt':
			core_http = 'http://localhost:8983/solr/txt'
			core = pysolr.Solr(core_http)
			CommitDataToSolr.add_txt(absolute_path, core, core_http)
		elif suffix == 'info':
			core_http = 'http://localhost:8983/solr/info'
			core = pysolr.Solr(core_http)
			CommitDataToSolr.add_info(absolute_path, core, core_http)
	else:
		CommitDataToSolr.SearchForFiles(absolute_path)


def Search():
	print 'Please input the key words you want to search for:'
	key_word = raw_input()
	print 'Please choose desc,txt,info or all to search:'
	type = raw_input()
	if type in ['desc', 'txt', 'info']:
		SolrSearch.SolrSearch(type, key_word)
	elif type == 'all':
		print '在desc库中查找结果如下：'
		SolrSearch.SolrSearch('desc', key_word)
		print '\n在txt库中查找结果如下：'
		SolrSearch.SolrSearch('txt', key_word)
		print '\n在info库中查找结果如下：'
		SolrSearch.SolrSearch('info', key_word)
	###这里仅实现了对单一关键词的搜索，后期还要加入多个关键词搜索，关键词之间用空格连接


def Usage():
	print 'Usage:'
	print '1、run script: python main.py'
	print '2、choose add, search, delete or help to type'
	return


def main():
	print "****************************************************" 
	print "***********Welcome to system for search*************"
	print "*Please input one of the words below to continue...*"
	print '*********', '\033[1;31;40madd     search    delete    help', '\033[0m*********'
	print "****************************************************" 

	if not os.path.exists('id_List.txt'):
		os.mknod('id_List.txt')
	command = raw_input()
	if command == 'add':
		Add()
	elif command == 'search':
		Search()
	elif command == 'delete':
		Delete_index()
	elif command == 'help':
		Usage()
	else:
		print 'ERROR!!!!!!'
		Usage()

if __name__ == '__main__':

	main()
