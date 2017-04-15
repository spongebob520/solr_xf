# encoding: utf-8
import uuid
import os
import hashlib

# 生成唯一的字符串序列作为info文件和txt文件索引的id序列
def Create_id():
	id_num =  str(uuid.uuid1())
	print id_num
	return id_num

# desc文件的id值
def Create_desc_id(file_path):
	sh1 = hashlib.sha1()
	sh1.update(file_path)
	id_num = sh1.hexdigest()
	return id_num
	

# 新建索引时候添加索引的路径、id、core、到列表中
def Create_list(file_path, id_num, core_http):
	id_list = []
	id_list.append([id_num, file_path, core_http])
	with open('id_List.txt', 'a+') as f:
		f.write(id_num + '\t' + file_path + '\t' + core_http + '\n')

# 删除列表中包含对应文件路径的行
def Delete_list_path(file_path):
	command = r"sed -i '/" + '\/'.join(file_path.split('/')) + r"/d'" + r' id_List.txt'
	os.system(command)

# 删除列表中包含指定id的行
def Delete_list_id(id_num):
	command = r"sed -i '/" + id_num + r"/d'" + r' id_List.txt'
	os.system(command)
