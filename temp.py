# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/python
#import PIL.Image as Image
#import pylab
#import skimage
import numpy as np
import os
from subprocess import call
from tqdm import tqdm
#import pandas as pd
import re
#视频的绝对路径和图片存储的目标路径
def extract_frames(src_path,target_path):

    new_path = target_path

    for video_name in tqdm(os.listdir(src_path)):
        #video_name = "clip1_010.mp4"
        filename = src_path + video_name
        cur_new_path = new_path+video_name.split('.')[0]+'/'
        if not os.path.exists(cur_new_path):
            os.makedirs(cur_new_path)
        #dest = cur_new_path + video_name.split('.')[0]+'-%04d.jpg'
        dest = cur_new_path +'%04d.jpg'
        #print('dest:', dest)
        #clip1_010-0001.jpg
        call(["ffmpeg", "-i", filename,"-vf","hqdn3d","-s","3840x2160", dest])
        #call(["ffmpeg", "-i", filename,"-vf","hqdn3d", dest]) 
        #ffmpeg -i $1"/"$file -vf hqdn3d -s 3840x2160 $2"/"$file

#生成对应视频帧的标签列表
def generate_list(frame_path):
    result = open("train.list",'w')
    for root_dir, dirs, files in os.walk(frame_path):
        print('root_dir:', root_dir)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件
        r = r"clip(.*)_"
        re_frame = re.compile(r)
        for frame_name in files:
            frame_path = root_dir+'/'+frame_name
            label = re.findall(re_frame,root_dir)[0] #对应帧的label
            result.write(frame_path+' '+str(label)+'\n')

if __name__ == '__main__':
    extract_frames(src_path='E:/汪萍黄珊/视频超分/SDR_540p/',target_path='E:/汪萍黄珊/视频超分/data_pics2/')
    #generate_list('E:/汪萍黄珊/视频超分/data_pics/')
