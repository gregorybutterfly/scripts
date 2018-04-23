"""Change the name of your favorite files in bulk.
Copy your files to 'images' directory and run the script with name argument.

>> python filename-changer.py -n NEWNAME
>> python filename-changer.py -n 'NEW NAME WITH SPACES'

"""

import os
import argparse

__AUTHOR__ = 'Grzegorz Motyl'
__PYTHON_VER__ = 'Python 3.5.2'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')


def create_img_directory():
    """Create 'images' directory to store files.
    """

    os.mkdir(os.path.join(BASE_DIR, 'images'))
    return


def file_list(directory):
    """List all files and add absolute path to each file for future usage.
    """

    files = os.listdir(directory)

    for i, file in enumerate(files):
        files[i] = os.path.join(directory, file)

    return files


def name_your_files(files, name, images_dir):
    """Rename your files
    """

    name = name.replace(' ', '_')

    # Change current directory to 'images'
    os.chdir(images_dir)

    for i, file in enumerate(files):
        old_file = file
        file = file.split('.')
        new_file = os.path.join(IMAGES_DIR, str(name) + '_' + str(i) + '.' + file[1])
        os.rename(old_file, new_file)

        print('Old name: {}'
              '\nNew name: {}'.format(old_file, new_file))


# Create images directory if not exist
if not os.path.isdir(IMAGES_DIR):
    create_img_directory()

# grab all elements and add absolute path to each file.
files = file_list(IMAGES_DIR)

# Create parser
parser = argparse.ArgumentParser(
    description='Change file names in bulk to save time and money :)'
)
parser.add_argument('-n','--name', help='New name for your files.', required=True)
args = vars(parser.parse_args())

if args['name']:
    # name your files
    name_your_files(files=files, name=args['name'], images_dir=IMAGES_DIR)
