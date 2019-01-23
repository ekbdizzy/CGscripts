# python 3.7
# Coding UTF-8

"""
Convert all *.mp4 files in folder to *.xvid with ffmpeg (http://ffmpeg.org/)
"""

import os
import subprocess as sp
import shutil

path = ''  # path to folder with video
ffmpeg = ''  # path to ffmpeg file

new_folder = os.path.join(path, 'mp4')
if not os.path.exists(os.path.join(path, new_folder)):
        os.mkdir(new_folder)

for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)):
        name = os.path.splitext(f)[0]
        new_name = name + '.avi'
        filepath = os.path.join(new_folder, f)
        shutil.move(os.path.join(path, f), os.path.join(new_folder, f))
        print(filepath)
        new_filepath = os.path.join(path, new_name)
        command = [ffmpeg,
                '-i', filepath,
                '-vcodec', 'mpeg4',
                '-q:v', '5',
                '-vtag', 'xvid', new_filepath]
        pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)
