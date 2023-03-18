import os
import xml.etree.ElementTree as ET

# xml文件存放目录(修改成自己的文件名)
input_dir = r'G:\XmlToTxt-master\VOC\Annotations'

# 输出txt文件目录（自己创建的文件夹）
out_dir = r'G:\\XmlToTxt-master\VOC\txt'

class_list = []


# 获取目录所有xml文件
def file_name(input_dir):
    F = []
    for root, dirs, files in os.walk(input_dir):

        for file in files:
            # print file.decode('gbk')    #文件名中有中文字符时转码
            if os.path.splitext(file)[1] == '.xml':
                t = os.path.splitext(file)[0]
                F.append(t)  # 将所有的文件名添加到L列表中
    return F  # 返回L列表


# 获取所有分类
def get_class(filelist):
    for i in filelist:
        f_dir = input_dir + "\\" + i + ".xml"
        in_file = open(f_dir, encoding='UTF-8')
        filetree = ET.parse(in_file)
        in_file.close()
        root = filetree.getroot()
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in class_list:
                class_list.append(cls)


def ConverCoordinate(imgshape, bbox):
    # 将xml像素坐标转换为txt归一化后的坐标
    xmin, xmax, ymin, ymax = bbox
    width = imgshape[0]
    height = imgshape[1]
    dw = 1. / width
    dh = 1. / height
    x = (xmin + xmax) / 2.0
    y = (ymin + ymax) / 2.0
    w = xmax - xmin
    h = ymax - ymin

    # 归一化
    x = x * dw
    y = y * dh
    w = w * dw
    h = h * dh

    return x, y, w, h


def readxml(i):
    f_dir = input_dir + "\\" + i + ".xml"

    txtresult = ''

    outfile = open(f_dir, encoding='UTF-8')
    filetree = ET.parse(outfile)
    outfile.close()
    root = filetree.getroot()

    # 获取图片大小
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    imgshape = (width, height)

    # 转化为yolov5的格式
    for obj in root.findall('object'):
        # 获取类别名
        obj_name = obj.find('name').text

        obj_id = class_list.index(obj_name)
        # 获取每个obj的bbox框的左上和右下坐标
        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text)
        xmax = float(bbox.find('xmax').text)
        ymin = float(bbox.find('ymin').text)
        ymax = float(bbox.find('ymax').text)
        bbox_coor = (xmin, xmax, ymin, ymax)

        x, y, w, h = ConverCoordinate(imgshape, bbox_coor)
        txt = '{} {} {} {} {}\n'.format(obj_id, x, y, w, h)
        txtresult = txtresult + txt

    # print(txtresult)
    f = open(out_dir + "\\" + i + ".txt", 'a')
    f.write(txtresult)
    f.close()


# 获取文件夹下的所有文件
filelist = file_name(input_dir)

# 获取所有分类
get_class(filelist)

# 打印class
print(class_list)

# xml转txt
for i in filelist:
    readxml(i)

# 在out_dir下生成一个class文件
f = open(out_dir + "\\classes.txt", 'a')
classresult = ''
for i in class_list:
    classresult = classresult + i + "\n"
f.write(classresult)
f.close()