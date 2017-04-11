# encoding: utf-8
import os
import pysolr
import SolrSearch
import CommitDataToSolr
import Delete
import sys

def Delete_index():
	print 'please choose ID NUMBER or ABSOLUTE PATH to delete'
	print 'input id or path '
	order = raw_input()
	if order == 'id':
		pass
	elif order == 'path':
	# 删除一个文件路径所创建的所有索引，适用于整个文件被删除的情况
		Check_Exists()	


def Core_Lists():
		pass

def Check_Exists():
	print 'Please input the absolute path of the file you want to delete'
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
	print 'Please input the absolute path of the file you want to add' 
	absolute_path = raw_input()

	if not os.path.exists(absolute_path):
		print 'the path does not exists'
		sys.exit(-1)
	elif os.path.isfile(absolute_path):
		suffix = absolute_path.split('.')[-1]
		if suffix == 'desc':
			CommitDataToSolr.add_desc(absolute_path)
		elif suffix == 'txt':
			CommitDataToSolr.add_txt(absolute_path)
		elif suffix == 'info':
			CommitDataToSolr.add_info(absolute_path)
	else:
		CommitDataToSolr.SearchForFiles(absolute_path)


def Search():
	print 'Please input the key words you want to search for'
	key_word = raw_input()
	print 'Please choose desc,txt,info or all to search\n'
	type = raw_input()
	if type == 'desc' or 'txt' or 'info':
		SolrSearch.SolrSearch(type, key_word)
	elif type == 'all':
		SolrSearch.SolrSearch('desc', key_word)
		SolrSearch.SolrSearch('txt', key_word)
		SolrSearch.SolrSearch('info', key_word)
	###这里仅实现了对单一关键词的搜索，后期还要加入多个关键词搜索，关键词之间用空格连接


def Useage():
	pass


def main():
	print "********************************************" 
	print "*********Welcome to system for search**********"
	print "*Please input one of the words below to continue...*"
	print "******add     search    delete    help*******"
	print "********************************************" 

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
	desc_list = {}
	info_list = {}
	txt_list = {}
	main()
