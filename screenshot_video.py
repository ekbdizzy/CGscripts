# python 3.7
# Coding UTF-8

"""
Creating screenshots with time you want for all videos in folders.
You need ffmpeg (http://ffmpeg.org/)

Two variants in input:
    'create' - creates screenshot
    'del' - delete all screenshot
    another input - exit
"""

import os
import subprocess as sp

path = r''  # path to folder with video files
ffmpeg = r'D:\Distrib\ffmpeg\bin\ffmpeg.exe'
video_ext = ['mp4', 'avi', 'wmv', 'mxf']  # format video you need to make screenshot
time = ['00:00:02.000', '00:00:06.000']  # frames to screenshot in format Hour:Minute:Second.millisecond


def create_dir(path, name):
    if not os.path.exists(os.path.join(path, name)):
        os.mkdir(os.path.join(path, name))


def create_screenshots(path):

    # All subfolders
    list_dir = [i[0] for i in os.walk(path)]

    for i in list_dir:
        i_path = os.listdir(os.path.join(path, i))
        for j in i_path:
            j_path = os.path.join(os.path.join(path, i), j)
            if os.path.isfile(j_path) and j_path[-3:] in video_ext:
                create_dir(i, 'preview_scr')
                preview_folder = os.path.join(i, 'preview_scr')
                for t in range(len(time)):
                    jpg_name = j_path[:-4] + str(t + 1) + '.jpg'
                    jpg_path = os.path.join(preview_folder, j[:-4]) + str(t + 1) + '.jpg'
                    command = [
                        ffmpeg,
                        '-i', j_path,
                        '-ss', time[t],
                        '-vframes', '1',
                        jpg_path
                    ]
                    print(jpg_path)
                    pipe = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)
    print('Created')


def del_screenshots(path):
    list_dir = [i[0] for i in os.walk(path)]
    for folder in list_dir:
        # folder_path = os.listdir(os.path.join(path, folder))
        if (folder[-11:]) == 'preview_scr':
            for file in os.listdir(folder):

                print(os.path.join(folder, file))
                os.remove(os.path.join(folder, file))
            os.rmdir(folder)
    print('Deleted')


inp = input('create or del: ')

if inp == 'del':
    del_screenshots(path)
elif inp == 'create':
    create_screenshots(path)
else:
    print('Stopped. Print "create" or "del"')
