# python 3.7
# Coding UTF-8

"""
Convert *.mp4 files to [avi 16:9 and 4:3],
[mxf 16:9 and 4:3] and HD_MXF_1080 with ffmpeg (http://ffmpeg.org/)
"""

import os
import subprocess as sp
import shutil
from create_folder import create_folder

path = r''  # folder with mp4 files
ffmbc = r'..\ffmpeg\bin\ffmbc.exe'  # path to ffmbc file
ffmpeg = r'..\ffmpeg\bin\ffmpeg.exe'  # path to ffmpeg file
formats = ['mxf', 'avi', 'HD', 'preview']


class ConvertVideo(object):
    def __init__(self):
        self.path = path
        self.formats = formats
        self.avi_formats = ['4', '16']
        self.mxf_formats = ['4', '16']
        self.HD_formats = ['HD']

    def convert_to_mxf(self):

        # create folders
        create_folder('mxf', path)
        for format_mxf in self.mxf_formats:
            convert_to_mxf_path = os.path.join(self.path, 'mxf', format_mxf)
            create_folder(convert_to_mxf_path, self.path)

        # convert to mxf
        for format_mxf in self.mxf_formats:
            for filename in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, filename)):
                    file_source = os.path.join(self.path, filename)
                    file_mxf_name = os.path.splitext(filename)[0] + '_' + format_mxf + '.mxf'
                    mxf_folder = os.path.join(self.path, 'mxf', format_mxf)
                    file_mxf_path = os.path.join(mxf_folder, file_mxf_name)
                    cropped_file = os.path.join(self.path, os.path.splitext(filename)[0] + '_cropped.mp4')

                    crop = [ffmpeg, '-i', file_source, '-vf', 'scale=720:445,pad=720:608:0:97:black',\
                            '-c:a', 'copy', cropped_file]

                    command_mxf_4 = [ffmbc,
                        '-i', cropped_file, '-target', 'imx50', '-aspect', '4:3', '-an',
                        file_mxf_path, '-acodec', 'pcm_s16le', '-ar', '48000', '-newaudio',
                        '-acodec', 'pcm_s16le', '-ar', '48000', '-y']

                    command_mxf_16 = [ffmbc,
                        '-i', file_source, '-target', 'imx50', '-aspect', '16:9', '-an',
                        file_mxf_path, '-acodec', 'pcm_s16le', '-ar', '48000', '-newaudio',
                        '-acodec', 'pcm_s16le', '-ar', '48000', '-y']

                    sp.call(crop)

                    if format_mxf == '4':
                        sp.call(command_mxf_4)
                    elif format_mxf == '16':
                        sp.call(command_mxf_16)

                    os.remove(cropped_file)

        print('MXF convert success!')

    def convert_to_avi(self):

        # create folders
        create_folder('avi', path)
        for format_avi in self.avi_formats:
            convert_to_avi_path = os.path.join(self.path, 'avi', format_avi)
            create_folder(convert_to_avi_path, self.path)

        # convert to avi
        for format_avi in self.avi_formats:
            for filename in os.listdir(self.path):
                if os.path.isfile(os.path.join(self.path, filename)):
                    file_source = os.path.join(self.path, filename)
                    file_avi_name = os.path.splitext(filename)[0] + '_' + format_avi + '.avi'
                    avi_folder = os.path.join(self.path, 'avi', format_avi)
                    file_avi_path = os.path.join(avi_folder, file_avi_name)
                    cropped_file = os.path.join(self.path, os.path.splitext(filename)[0] + '_cropped.mp4')

                    crop = [ffmpeg, '-i', file_source, '-vf', 'scale=720:445,pad=720:608:0:97:black', \
                            '-c:a', 'copy', cropped_file]

                    command_avi_4 = [ffmpeg, '-i', cropped_file, '-s', '720:576', '-aspect', '4:3', '-vf', 'crop=720', '-vcodec', \
                                     'dvvideo', '-acodec', 'pcm_s16le', '-ac', '2', '-y', file_avi_path]

                    command_avi_16 = [ffmpeg, '-i', file_source, '-s', '720:576', '-aspect', '16:9', '-vf', 'crop=1920', '-vcodec', \
                                     'dvvideo', '-acodec', 'pcm_s16le', '-ac', '2', '-y', file_avi_path]

                    sp.call(crop)

                    if format_avi == '4':
                        sp.call(command_avi_4)
                    elif format_avi == '16':
                        sp.call(command_avi_16)

                    os.remove(cropped_file)

        print('Avi convert success!')

    def convert_to_mxf_HD(self):

        # create folders
        create_folder('HD', path)

        for filename in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, filename)):
                file_source = os.path.join(self.path, filename)
                file_HD_name = os.path.splitext(filename)[0] + '_HD' + '.mxf'
                HD_folder = os.path.join(self.path, 'HD')
                file_HD_path = os.path.join(HD_folder, file_HD_name)

                command_HD = [ffmbc, '-i', file_source, '-threads', '4', '-tff', '-target', 'xdcamhd422', \
                              '-f', 'mxf', '-an', file_HD_path,'-y','-acodec', 'pcm_s16le', '-ar', '48000', \
                              '-newaudio', '-acodec', 'pcm_s16le', '-ar', '48000', '-newaudio',
                              '-map' + '_' + 'audio' + '_' + 'channel', '0:1:0:0:1:0', '-map' + '_' + 'audio' + '_' + 'channel', '0:1:0:0:2:0']

                sp.call(command_HD)

        print('HD convert success!')

    def copy_to_preview(self):

        create_folder('preview', self.path)
        for filename in os.listdir(self.path):
            file_source = os.path.join(self.path, filename)
            if os.path.isfile(file_source) and os.path.splitext(file_source)[1] == '.mp4':
                file_preview = os.path.join(os.path.join(path, 'preview'), filename)
                shutil.move(file_source, file_preview)

# initialize converter
converter = ConvertVideo()

# check formats you need
converter.convert_to_mxf_HD()
converter.convert_to_mxf()
converter.convert_to_avi()
converter.copy_to_preview()
