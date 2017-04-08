#encoding: utf-8

import os
import pysolr


# txt文档为结构化文档，只有两列和四列的区分，当列数为其他情况时候，不做处理
def add_txt(files_path)
    solr = pysolr.Solr('http://localhost:8983/solr/' + 'gettingstarted_shard1_replica2')
    with open(files_path, 'rb') as f:
        dicts = []
        for line in f:
            words = line.strip().split()
            #引入全路径作为该文件的标识，该文件中所有行共用这一个标识，方便之后删除索引操作
            words.append(os.path.abspath(files_path))
            if len(words == 5):
                fields = ('wav', 'start', 'end', 'text', 'path')
            elif len(words == 3)：
                fields = ('start', 'end', 'path')
            else:
                print 'ERROR!' + files_path + 'is not the correct format!'
                break

            dicts.append(dict(zip(fields, words)))

        solr.add(dicts)


def add_info(files_path):
    solr = pysolr.Solr('http://localhost:8983/solr/' + 'gettingstarted_shard1_replica2')
    with open(files_path, 'rb') as f:
        dicts = []
        i = 0
        for line in f:
            words = line.strip().split()
            # 引入全路径作为该文件的标识，该文件中所有行共用这一个标识，方便之后删除该文件内左右索引
            words.append(os.path.abspath(files_path))
            if i == 0:
                fields = words
            else:
                dicts.append(dict(zip(fields, words)))
            i += 1
        solr.add(dicts)

def add_desc(files_path):
    solr = pysolr.Solr('http://localhost:8983/solr/' + 'gettingstarted_shard1_replica2')
    with open(files_path, 'rb') as f:
        id = Random_id.Random_id(files_path, id_list)
        text = f.readlines()
        solr.add([{'id': id,
                   'fields': text
                }])


def SearchForFiles(Home_dir,current_path):
    for path, folder, files in os.walk(Home_dir):
        for filename in files:
            files_path=os.path.join(path, filename)
            print files_path
            postfix = files_path.strip().split('/')[-1].split('.')[-1]
            id_num = files_path.strip().split('/')[3]
            print id_num
            if postfix == 'desc':
                print files_path
                add_desc(files_path)
            elif postfix == 'txt':
                add_txt(files_path)
            elif postfix == 'info':
                add_txt(files_path)
            else:
                continue


if __name__ == '__main__':
    # url = 'http://10.20.0.71:8983/solr/gettingstarted/update'
    Home_dir = os.getcwd()
    current_path = os.getcwd()
    print Home_dir
    print current_path 
    SearchForFiles(Home_dir,current_path)

