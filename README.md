# 基于全文检索数据查询工具

支持对数据描述文件（desc）、属性文件（info）、标注文件（txt）以及 doc 目录下的文件（含富文本文件）进行全文检索；

--------------------------------------------------------------------------------
1、solr启动操作：
   bin/solr start
   bin/solr create -c <新核的名称，如：desc,info等>

-------------------------------------------------------------------------------   
2、查询工具操作方法：
    main.py是主脚本，运行时候只需运行该脚本即可
    运行main.py脚本以后，可以通过键入add,search,delete来进行相应操作
--------------------------------------------------------------------------------

3、主要API介绍：

--建立（更新）索引：
      CommitDataToSolr.add_desc():对desc文件建立索引；
      CommitDataToSolr.add_info():对info文件按行建立索引；
      CommitDataToSolr.add_txt():对txt文件按行建立索引；

--删除索引：
      按id删除索引：Delete.Delete_id()
      按path删除索引：
                      Delete.Delete_desc():删除desc文件的索引
                      Delete.Delete_info():删除info文件的索引
                      Delete.Delete_txt():删除txt文件的索引
      一键删除所有索引：
                      Delete.Delete_all()

--按索引查找：
      SolrSearch.SolrSearch()
-------------------------------------------------------------------------------
补充：
1、id_List.Create_list()会创建id_List.txt文件，记录了唯一id号，文件路径和所属核；
2、在建立索引时候，会在该文件中创建一行对应的信息，在更新索引时候也会对应更新该文件，在删除索引时候也会删除该文件中的对应行。
