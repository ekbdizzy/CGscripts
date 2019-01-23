# python 3.7
# Coding UTF-8

"""
Create folder in path, if it not exists
"""

import os

def create_folder(name, path):
    if not os.path.exists(os.path.join(path, name)):
        os.mkdir(os.path.join(path, name))
    else:
        print(f'Folder {os.path.join(path, name)} is already exists')
