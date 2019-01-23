# python 3.7
# Coding UTF-8

"""
Find your absent files in folder, check it with *.txt file
"""

import os

text_path = r'indexes.txt'  # file with files paths you need
files_path = r''  # folder with files to check
file_names = os.listdir(files_path)

with open(text_path) as file:
    text = file.read().strip().split('\n')
files = list(map(lambda x: x.split('.')[0], file_names))

result = list(set(text) ^ set(files))
print(result)  # list of absent files in folder
