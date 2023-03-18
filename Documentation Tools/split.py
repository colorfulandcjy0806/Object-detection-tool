import os
import random
import shutil

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def getData(src_path):

    dest_dir = src_path+'un' #划分出来的验证集
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list) * 0.25)  # 这个可以修改划分比例
    for f in img_list[le:]:
        shutil.move(f, dest_dir)


'''
函数功能：
划分数据集
'''
def SplitImg(filePath):
    getData(filePath)

'''
函数功能：
根据划分的数据集进行移动标注文件
'''
def MoveAn(filePathAn,filePathImg):
    Imgs=os.listdir(filePathImg)
    if not os.path.isdir(filePathAn+'un'):
        os.mkdir(filePathAn+'un')

    for file in os.listdir(filePathAn):
        #print(filePathAn,filePathImg)
        #print(os.path.join(filePathAn,file),os.path.join(filePathAn+'un',file))
        if file[:-4]+'.jpg' in Imgs:

            shutil.move(os.path.join(filePathAn,file),os.path.join(filePathAn+'un',file))

if __name__=='__main__':
    filePath='img'# 换成你的数据集

    #拆分的数据集
    SplitImg(filePath)
    filePathAn='txt'# 换成你的标注文件地址

    # 根据数据集进行移动标注文件
    MoveAn(filePathAn,filePath+'un')
