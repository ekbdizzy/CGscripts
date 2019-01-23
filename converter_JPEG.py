# python 3.7
# Coding UTF-8

"""
Convert all CMYK *.tif files in folder to jpeg with resize
You need ImageMagick (https://imagemagick.org/)
"""


import os
import shutil
import subprocess as sp

dir_path = r''  # path to folder with tif files
convert = r''  # Program Files\ImageImageMagick-7.0.7-Q16\convert.exe
jpegicc = r''  # ImageMagick_PATH\lcms-1.18a.win.bin\bin\jpegicc.exe
resize = '1200'  # width of final jpeg file (must be string)

for file in os.listdir(dir_path):
    file_source = os.path.join(dir_path, file)
    if os.path.isfile(file_source) and file_source.split('.')[1] == 'tif':
        file_tmp_jpg = file_source.split('.')[0] + '_tmp' + '.jpg'
        file_jpg = file_source.split('.')[0] + '.jpg'
        convert_to_jpg = [convert, '-quality', '100', '-resize', resize, file_source, file_tmp_jpg]
        apply_icc = [jpegicc, '-q100', file_tmp_jpg, file_jpg]

        sp.call(convert_to_jpg)
        sp.call(apply_icc)
        os.remove(file_tmp_jpg)
