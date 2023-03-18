#coding:utf8
import os
from PIL import Image

def compress(src_path,dst_path,compress_rate=0.5):
    img = Image.open(src_path)
    w = int(img.size[0]*compress_rate)
    h = int(img.size[1]*compress_rate)
    img_resize = img.resize((w,h))
    img_resize.save(dst_path)

if __name__ == "__main__":
    src_dir = 'a'
    dst_dir = 'c'
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for filename in os.listdir(src_dir):
        img_path = os.path.join(src_dir,filename)
        new_img_path = os.path.join(dst_dir,filename)
        compress(img_path,new_img_path,0.5)
