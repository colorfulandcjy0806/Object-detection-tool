# -*- coding:utf-8 -*-

import  shutil
import os

oldpath = 'train2017'          # 原数据路径
newpath = 'img'       # 移动到新文件夹的路径
file_path = 'c.txt'       # txt中指定移动文件的文件信息

#从文件中获取要拷贝的文件的信息
def get_filename_from_txt(file):
    filename_lists = []
    with open(file,'r',encoding='utf-8') as f:
        lists =  f.readlines()
        for list in lists:
            # filename_lists.append(str(list).strip('\n')+'.jpg')
            filename_lists.append(str(list).strip('\n'))
    return filename_lists

#拷贝文件到新的文件夹中
def mycopy(srcpath,dstpath,filename):
    if not os.path.exists(srcpath):
        print("srcpath not exist!")
    if not os.path.exists(dstpath):
        print("dstpath not exist!")
    for root,dirs,files in os.walk(srcpath,True):

        if filename in files:
            # 如果存在就拷贝
            shutil.copy(os.path.join(root,filename),dstpath)
        else:
            # 不存在的话将文件信息打印出来
            print(filename)

if __name__ == "__main__":
    #执行获取文件信息的程序
    filename_lists = get_filename_from_txt(file_path)
    #根据获取的信息进行遍历输出
    for filename in filename_lists:
        mycopy(oldpath,newpath,filename)
