# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:17:04 2019

@author: lzhpc
"""

import numpy as np
import os
from subprocess import call
from tqdm import tqdm
#import pandas as pd
import re
#视频的绝对路径和图片存储的目标路径
def extract_frames(src_path,target_path):

    new_path = target_path

    for pictures_name in tqdm(os.listdir(src_path)):
        #video_name = "clip1_010.mp4"
        filename = src_path + pictures_name+'/'+'%04d.jpg'
        print('filename:', filename)
        cur_new_path = new_path+pictures_name.split('.')[0]+'/'
        print('cur_new_path:', cur_new_path)
        if not os.path.exists(cur_new_path):
            os.makedirs(cur_new_path)
        dest = cur_new_path + pictures_name.split('.')[0]+'.mp4'
        print('dest:', dest)
        #clip1_010-0001.jpg
        call(["ffmpeg", "-r","24000/1001","-i", filename,"-vcodec","libx265","-pix_fmt","yuv422p","-crf","10", dest]) 
        #ffmpeg -r 24000/1001 -i pngs/out%4d.png -vcodec libx265 -pix_fmt yuv422p -crf 10 test.mp4

if __name__ == '__main__':
    extract_frames(src_path='E:/汪萍黄珊/视频超分/data_pics/',target_path='E:/汪萍黄珊/视频超分/result/')