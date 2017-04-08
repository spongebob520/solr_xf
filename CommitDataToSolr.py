#encoding: utf-8

import os
import pysolr


# txt文档为结构化文档，只有两列和四列的区分，当列数为其他情况时候，不做处理
def add_txt(files_path, core):
	core.delete(q='path:' + os.path.abspath(files_path))
	dicts = []
    with open(files_path, 'rb') as f:
        for i, line in enumerate(f):
            words = [s.decode('utf-8') for s in line.strip().split()]
            if i == 0:
            	if len(words == 4):
                	fields = ('wav', 'start', 'end', 'text', 'path')
            	elif len(words == 2)：
                	fields = ('start', 'end', 'path')
            	else:
                	print 'ERROR!' + files_path + 'is not the correct format!'
			words.append(os.path.abspath(files_path))
            dicts.append(dict(zip(fields, words)))

        core.add(dicts)


def add_info(files_path, core):
	core.delete(q='path:' + os.path.abspath(files_path))
    with open(files_path, 'rb') as f:
        dicts = []
        for i, line in enumerate(f):
            words = [s.decode('utf-8') for s in line.strip().split()]
            if i == 0:
                fields = words[:]
				fields.extend([u'path', u'content'])
            else:
				words.extend([os.path.abspath(filename).decode('utf-8'), line.decode('utf-8')])
                dicts.append(dict(zip(fields, words)))
        core.add(dicts)

def add_desc(files_path, core):
	with open(files_path, 'rb') as f:
		text = f.read().decode('utf-8')
		core.add([{'id': os.path.abspath(files_path),
				   'context': text
				 }])


def SearchForFiles(Home_dir,current_path):
    for path, folder, files in os.walk(Home_dir):
        for filename in files:
            files_path=os.path.join(path, filename)
            print files_path
            postfix = files.split('.')[-1]

            if postfix == 'desc':
				core = 'http://localhost:8983/solr/desc'
                add_desc(files_path, core)
            elif postfix == 'txt':
				core = 'http://localhost:8983/solr/txt'
                add_txt(files_path, core)
            elif postfix == 'info':
				core = 'http://localhost:8983/solr/info'
                add_txt(files_path, core)


if __name__ == '__main__':
    # url = 'http://10.20.0.71:8983/solr/gettingstarted/update'
    Home_dir = os.getcwd()
    current_path = os.getcwd()
    print Home_dir
    print current_path 
    SearchForFiles(Home_dir,current_path)

