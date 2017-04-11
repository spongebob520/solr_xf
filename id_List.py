# encoding: utf-8
import uuid
import os

# 生成唯一的字符串序列作为一条索引的id序列
def Create_id():
	return uuid.uuid1()

# 新建索引时候添加索引的路径、id、core、到列表中
def Create_list(file_path, id_num, core):
	id_list = []
	id_list.append([id_num, file_path, core])
	with open('id_list.txt', 'a+') as f:
		f.write(id_num + file_path + core + '\n')

# 删除列表中包含对应文件路径的行
def Delete_list_path(file_path):
	with open('id_list.txt', '') as f:
		command = 'sed \'/' + file_path + '/d\'' + f
		os.system(command)

# 删除列表中包含指定id的行
def Delete_list_id(id_num):
	with open('id_list,txt', '') as f:
		command = 'sed \'/' + id_num + '/d\'' + f
		os.system(command)
