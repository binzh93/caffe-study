# -*- coding: utf-8 -*-
import commands


# generate lmda file by image_name and label  -- some params need to set
# 1: convert_imageset_path: your caffe setup path
# 2: resize size
# 3: image and label txt file list path
# 4: image data path
# 5: lmdb save path
def create_db(txt_save_path, images_path, lmdb_save_path):
    convert_imageset_path = '/home/ubuntu/caffe/' + "build/tools/convert_imageset"
    cmd = """%s --shuffle --resize_height=256 --resize_width=256 %s %s %s"""       
    status, output = commands.getstatusoutput(cmd % (convert_imageset_path, images_path,
        txt_save_path, lmdb_save_path))
    print output
    if(status == 0):
        print "lmbd文件生成成功"

if __name__ == '__main__':
    txt_save_path = "/data/pycaffe-file/validation_list.txt"
    images_path = "/data/image_scene_training/data/"
    lmdb_save_path = '/data/pycaffe-file/validation.lmdb'
    create_db(txt_save_path, images_path, lmdb_save_path)
