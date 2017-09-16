"""
Scan a folder and grab all its files. Check modification time of each file and compare it with previously collected data

SCANNING(BASE_DIR):
if file: append files list
if dir: SCANNING(DIR)

"""

from os import path, listdir, stat
from time import sleep

# time between each check
t = 5

# base dir for scanning.
BASE_DIR = None
if not BASE_DIR:
    BASE_DIR = path.abspath('.')

# grab all files from base_dir and subdirectories.
files = []


def scanning(p):
    """ Scan base_dir and subdirs for files """
    for file in listdir(p):
        if path.isdir(path.join(p, file)):
            scanning(path.join(p, file))
        elif path.isfile(path.join(p, file)):
            files.append(path.join(p, file))


scanning(BASE_DIR)

# dict: key=file path, value=modification time
files_dict = {k: stat(k).st_mtime for k in files}

# grab an element from files list, check modification time and compare it with existing data from files_dict
while True:
    sleep(t)
    for element in files:
        old = files_dict.get(element)
        new = stat(element).st_mtime

        if old == new:
            continue
        else:
            print('Changed: ', element)
            files_dict[file] = new
