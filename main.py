import os
import pysolr
import SolrSearch
import CommitDataToSolr
import hashlib
import Delete



#create unique id_num for every absolute_path
def Random_Id(absolute_path):
	global id_list
	sh1 = hashlib.sha1()
	sh1.update(absolute_path)
	id_list[absolute_path] = sh1.hexdigest()


def Check_Exists(command):
	print 'Please input the absolute path of the file you want to add/delete'
	absolute_path == raw_input()
	# check whether the path exists
	if command == 'add':
		if not os.path.exists(absolute_path):
			print 'the path does not exists'
			sys.exit(-1)
		# if the path is a file,check whether the file exists,yes => 'update',no => 'add'
		elif os.path.isfile(absolute_path):
			if absolute_path in id_list:
				print 'the file ' + absolute_path + ' is already exists,update it'
				Update(absolute_path)
			else:
				Add()
		# if the path is a folder,go through the folder and check every file in it to update or add
		else:
			file_lists = CommitDataToSolr.SearchForFiles(absolute_path)
			for file in file_lists:
				if file in id_list:
					print 'the file ' + file + ' is already exists,update it'
					Update(file)
				else:
					Add()
	else:
		if not os.path.exists(absolute_path):
			print'the path does not exists'
			sys.exit(-1)
		else:
			Delete()

def Search():
	print 'Please input the key words you want to search for'
	key_word == raw_input()
	SolrSearch.SolrSearch(key_word)
	###这里仅实现了对单一关键词的搜索，后期还要加入多个关键词搜索，关键词之间用空格连接


def Useage():
	pass


def main():
	print "********************************************" 
	print "*********Welcome to system for search**********"
	print "*Please input one of the words below to continue...*"
	print "******add    update    search    delete    help*******"
	print "********************************************" 

	command = raw_input()
	if command == 'add':
		Check_Exists(command)
	elif command == 'update':
		Update()
	elif command == 'search':
                Search()
	elif command == 'delete':
		Check_Exists(command)
	elif command == 'help':
		Usage()
	else:
		print 'ERROR!!!!!!'
		Usage()

if __name__ == '__main__':
	id_list = {}
	main()
