import os
import codecs# 读取文件夹中的文件名
folder = 'train'
filenames = os.listdir(folder)
 
# 将文件名写入 txt 文件
txt_file = 'train.txt'
with codecs.open(txt_file, 'w', 'utf-8') as f:
    for filename in filenames:
        f.write("./images/train/"+filename + '\n')
